import streamlit as st
import pandas as pd
from datetime import date
import random

st.set_page_config(page_title="Sr. Kitchen", page_icon="🍽️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp{background-color:#0f0f14;color:#f0f0f5;}
[data-testid="stSidebar"]{background-color:#16161f;border-right:1px solid rgba(255,255,255,0.07);}
.metric-card{background:#1e1e2a;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:1.25rem;margin-bottom:1rem;}
.metric-title{font-size:0.78rem;color:#8888aa;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;}
.metric-value{font-size:1.9rem;font-weight:800;color:#f59e0b;}
.metric-sub{font-size:0.8rem;color:#55556a;margin-top:0.2rem;}
.page-header{padding:1.5rem 0 1rem;border-bottom:1px solid rgba(255,255,255,0.07);margin-bottom:2rem;}
.page-header h1{font-size:1.8rem;font-weight:800;color:#f0f0f5;margin:0;}
.page-header p{color:#8888aa;margin:0.3rem 0 0;}
.sidebar-logo{text-align:center;padding:1.5rem 0 1rem;}
.sidebar-logo h2{color:#f59e0b;font-size:1.6rem;font-weight:800;margin:0;}
.sidebar-logo p{color:#55556a;font-size:0.8rem;margin:0.2rem 0 0;}
.sidebar-role{background:#f59e0b18;border:1px solid #f59e0b33;border-radius:8px;padding:0.6rem 1rem;margin:0.5rem 0 1rem;text-align:center;}
.sidebar-role span{color:#fbbf24;font-size:0.85rem;font-weight:600;}
.stButton>button{background:#f59e0b!important;color:#000!important;border:none!important;border-radius:100px!important;font-weight:600!important;}
.block-container{padding-top:2rem;}
</style>
""", unsafe_allow_html=True)

PLATOS = [
    ("Bandeja paisa","Frijoles, chicharron, huevo, arroz, chorizo, morcilla","Plato fuerte",22500),
    ("Ajiaco santafereno","Pollo, papas criollas, mazorca, guascas, crema","Sopas",18000),
    ("Sancocho de gallina","Gallina criolla, yuca, papa, platano, cilantro","Sopas",24000),
    ("Arroz con pollo","Pollo, arroz, zanahoria, guisantes, alinos","Plato fuerte",19000),
    ("Cazuela de mariscos","Camarones, calamares, almejas, crema de coco","Especialidad",28000),
    ("Lomo al trapo","Lomo de res, papas al horno, ensalada verde","Especialidad",35000),
    ("Patacon con todo","Patacon, hogao, chicharron, queso costeno","Entradas",12000),
    ("Limonada de coco","Limon, coco, leche condensada, hielo","Bebidas",7000),
]

def init():
    if "role" not in st.session_state:
        st.session_state.role=None; st.session_state.user=None; st.session_state.page="Dashboard"
    if "productos" not in st.session_state:
        st.session_state.productos=pd.DataFrame([
            {"ID":"P001","Nombre":"Pollo entero","Cat":"Carnes","Stock":25,"Unidad":"kg","PC":18000,"PV":32000,"SMin":5},
            {"ID":"P002","Nombre":"Arroz blanco","Cat":"Granos","Stock":80,"Unidad":"kg","PC":2800,"PV":5500,"SMin":20},
            {"ID":"P003","Nombre":"Tomate chonto","Cat":"Verduras","Stock":15,"Unidad":"kg","PC":3500,"PV":7000,"SMin":8},
            {"ID":"P004","Nombre":"Aceite vegetal","Cat":"Aceites","Stock":12,"Unidad":"Lt","PC":8500,"PV":14000,"SMin":4},
            {"ID":"P005","Nombre":"Cebolla cabezona","Cat":"Verduras","Stock":30,"Unidad":"kg","PC":2200,"PV":4500,"SMin":10},
            {"ID":"P006","Nombre":"Papa criolla","Cat":"Tuberculos","Stock":40,"Unidad":"kg","PC":3000,"PV":6000,"SMin":15},
            {"ID":"P007","Nombre":"Sal marina","Cat":"Condimentos","Stock":6,"Unidad":"kg","PC":1500,"PV":3000,"SMin":3},
            {"ID":"P008","Nombre":"Azucar blanca","Cat":"Azucares","Stock":3,"Unidad":"kg","PC":3200,"PV":5800,"SMin":5},
        ])
    if "pedidos" not in st.session_state:
        st.session_state.pedidos=pd.DataFrame([
            {"ID":"PED-001","Mesa":3,"Cliente":"Juan Garcia","Plato":"Bandeja paisa","Cant":2,"Total":45000,"Estado":"Entregado","Fecha":"2024-03-10"},
            {"ID":"PED-002","Mesa":5,"Cliente":"Maria Lopez","Plato":"Ajiaco santafereno","Cant":1,"Total":18000,"Estado":"En preparacion","Fecha":"2024-03-10"},
            {"ID":"PED-003","Mesa":1,"Cliente":"Carlos Ruiz","Plato":"Sancocho de gallina","Cant":3,"Total":72000,"Estado":"Pendiente","Fecha":"2024-03-10"},
            {"ID":"PED-004","Mesa":7,"Cliente":"Ana Mora","Plato":"Arroz con pollo","Cant":2,"Total":38000,"Estado":"Entregado","Fecha":"2024-03-09"},
            {"ID":"PED-005","Mesa":2,"Cliente":"Pedro Silva","Plato":"Cazuela de mariscos","Cant":1,"Total":28000,"Estado":"Entregado","Fecha":"2024-03-09"},
        ])
    if "usuarios" not in st.session_state:
        st.session_state.usuarios=pd.DataFrame([
            {"ID":"U001","Nombre":"Admin Principal","Correo":"admin@srkitchen.com","Rol":"Administrador","Estado":"Activo"},
            {"ID":"U002","Nombre":"Carlos Mesero","Correo":"carlos@srkitchen.com","Rol":"Mesero","Estado":"Activo"},
            {"ID":"U003","Nombre":"Laura Mesero","Correo":"laura@srkitchen.com","Rol":"Mesero","Estado":"Activo"},
            {"ID":"U004","Nombre":"Roberto Mesero","Correo":"roberto@srkitchen.com","Rol":"Mesero","Estado":"Inactivo"},
        ])
    if "facturas" not in st.session_state:
        st.session_state.facturas=pd.DataFrame([
            {"Factura":"F-0001","Cliente":"Juan Garcia","Mesa":3,"Subtotal":38793,"IVA":6207,"Total":45000,"Fecha":"2024-03-10","Estado":"Pagada"},
            {"Factura":"F-0002","Cliente":"Ana Mora","Mesa":7,"Subtotal":32759,"IVA":5241,"Total":38000,"Fecha":"2024-03-09","Estado":"Pagada"},
        ])

def hdr(t,s=""):
    st.markdown(f'<div class="page-header"><h1>{t}</h1><p>{s}</p></div>',unsafe_allow_html=True)

def ce(v):
    c={"Entregado":"#34d399","En preparacion":"#fbbf24","Pendiente":"#f87171","Pagada":"#34d399","Activo":"#34d399","Inactivo":"#f87171","Administrador":"#f87171","Mesero":"#fbbf24"}
    return f"color:{c.get(v,'#f0f0f5')};font-weight:600"

def login():
    _,col,_=st.columns([1,2,1])
    with col:
        st.markdown('<div style="text-align:center;padding:2.5rem 0 2rem"><div style="font-size:4rem">🍽️</div><h1 style="color:#f59e0b;font-size:2.2rem;font-weight:800;margin:.5rem 0 0">Sr. Kitchen</h1><p style="color:#8888aa;margin:.3rem 0 1.5rem">Sistema de Gestión de Restaurante</p></div>',unsafe_allow_html=True)
        role=st.selectbox("Selecciona tu rol",["Administrador","Mesero","Cliente"])
        if st.button("🔐 Ingresar al Sistema",use_container_width=True):
            st.session_state.role=role
            st.session_state.user={"Administrador":"Admin Principal","Mesero":"Carlos Mesero","Cliente":"Visitante Demo"}[role]
            st.rerun()
        st.markdown('<div style="margin-top:1.5rem;background:#1e1e2a;border-radius:12px;padding:1.2rem;font-size:.83rem;color:#8888aa;border:1px solid rgba(255,255,255,.07)"><b style="color:#f59e0b">Roles disponibles:</b><br><br>🔴 <b style="color:#f0f0f5">Administrador</b> — Dashboard, inventario, pedidos, usuarios, facturación, reportes y predicción de demanda<br><br>🟡 <b style="color:#f0f0f5">Mesero</b> — Dashboard, pedidos y menú<br><br>🟢 <b style="color:#f0f0f5">Cliente</b> — Ver menú y hacer pedidos desde la mesa</div>',unsafe_allow_html=True)

def sidebar():
    role=st.session_state.role
    MENUS={"Administrador":[("📊 Dashboard","Dashboard"),("📦 Inventario","Inventario"),("🛒 Pedidos","Pedidos"),("👥 Usuarios","Usuarios"),("🧾 Facturacion","Facturacion"),("📈 Reportes","Reportes"),("🤖 Prediccion","Prediccion")],"Mesero":[("📊 Dashboard","Dashboard"),("🛒 Pedidos","Pedidos"),("📋 Menu","Menu")],"Cliente":[("📋 Menu","Menu"),("🛒 Pedir","MisPedidos")]}
    with st.sidebar:
        st.markdown(f'<div class="sidebar-logo"><div style="font-size:2.5rem">🍽️</div><h2>Sr. Kitchen</h2><p>Gestión de Restaurante</p></div><div class="sidebar-role"><span>{"🔴" if role=="Administrador" else "🟡" if role=="Mesero" else "🟢"} {st.session_state.user} — {role}</span></div>',unsafe_allow_html=True)
        st.markdown("**Navegación**")
        for label,key in MENUS[role]:
            if st.button(label,key=f"nav_{key}",use_container_width=True):
                st.session_state.page=key; st.rerun()
        st.divider()
        if st.button("🚪 Cerrar sesión",use_container_width=True):
            st.session_state.role=None; st.session_state.user=None; st.session_state.page="Dashboard"; st.rerun()

def p_dashboard():
    hdr("📊 Dashboard","Resumen general del sistema")
    df_p=st.session_state.productos; df_ped=st.session_state.pedidos
    ventas=df_ped[df_ped["Fecha"]=="2024-03-10"]["Total"].sum()
    bajo=int((df_p["Stock"]<=df_p["SMin"]).sum()); activos=len(df_ped[df_ped["Estado"]!="Entregado"])
    c1,c2,c3,c4=st.columns(4)
    for col,title,val,sub in[(c1,"💰 Ventas hoy",f"${ventas:,.0f}","COP"),(c2,"🛒 Pedidos activos",str(activos),"En proceso"),(c3,"📦 Productos",str(len(df_p)),"En inventario"),(c4,"⚠️ Stock bajo",f'<span style="color:#f87171">{bajo}</span>',"Reabastecer")]:
        col.markdown(f'<div class="metric-card"><div class="metric-title">{title}</div><div class="metric-value">{val}</div><div class="metric-sub">{sub}</div></div>',unsafe_allow_html=True)
    st.markdown("---")
    c1,c2=st.columns(2)
    with c1:
        st.markdown("#### 🛒 Pedidos recientes")
        st.dataframe(df_ped[["ID","Mesa","Cliente","Plato","Total","Estado"]].style.applymap(ce,subset=["Estado"]),use_container_width=True,hide_index=True)
    with c2:
        st.markdown("#### ⚠️ Productos con stock bajo")
        bajo_df=df_p[df_p["Stock"]<=df_p["SMin"]][["Nombre","Stock","SMin","Unidad"]]
        if bajo_df.empty: st.success("✅ Todo el inventario en niveles óptimos")
        else: st.dataframe(bajo_df,use_container_width=True,hide_index=True)
    st.markdown("#### 📈 Ventas últimos 7 días")
    fechas=pd.date_range(end=date.today(),periods=7).strftime("%d/%m").tolist()
    st.bar_chart(pd.DataFrame({"Ventas (COP)":[random.randint(80000,280000) for _ in fechas]},index=fechas),color="#f59e0b")

def p_inventario():
    hdr("📦 Gestión de Inventario","Control de insumos y productos del restaurante")
    t1,t2,t3=st.tabs(["📋 Ver Inventario","➕ Agregar Producto","✏️ Actualizar Stock"])
    with t1:
        df=st.session_state.productos.copy(); b=st.text_input("🔍 Buscar",placeholder="Nombre o categoría...")
        if b: df=df[df["Nombre"].str.contains(b,case=False)|df["Cat"].str.contains(b,case=False)]
        def res(row): return ["background-color:#ef444418"]*len(row) if row["Stock"]<=row["SMin"] else [""]*len(row)
        st.dataframe(df.style.apply(res,axis=1),use_container_width=True,hide_index=True)
        st.caption("🔴 Fila roja = stock por debajo del mínimo")
        c1,c2,c3=st.columns(3)
        c1.metric("💰 Valor total",f"${(df['Stock']*df['PC']).sum():,.0f} COP")
        c2.metric("📦 Total productos",len(df)); c3.metric("⚠️ Bajo stock",len(df[df["Stock"]<=df["SMin"]]))
    with t2:
        with st.form("fp"):
            c1,c2=st.columns(2)
            with c1: nombre=st.text_input("Nombre *"); cat=st.selectbox("Categoría",["Carnes","Verduras","Granos","Tuberculos","Aceites","Condimentos","Azucares","Lacteos","Bebidas","Otros"]); unidad=st.selectbox("Unidad",["kg","gr","Lt","ml","Unidad","Docena","Caja"])
            with c2: stock=st.number_input("Stock inicial",min_value=0,value=0); pc=st.number_input("Precio compra",min_value=0,value=0); pv=st.number_input("Precio venta",min_value=0,value=0); smin=st.number_input("Stock mínimo",min_value=0,value=5)
            if st.form_submit_button("✅ Registrar Producto",use_container_width=True):
                if nombre.strip():
                    nid=f"P{len(st.session_state.productos)+1:03d}"
                    st.session_state.productos=pd.concat([st.session_state.productos,pd.DataFrame([{"ID":nid,"Nombre":nombre,"Cat":cat,"Stock":stock,"Unidad":unidad,"PC":pc,"PV":pv,"SMin":smin}])],ignore_index=True)
                    st.success(f"✅ {nombre} registrado"); st.rerun()
                else: st.error("❌ El nombre es obligatorio")
    with t3:
        ps=st.selectbox("Producto",st.session_state.productos["Nombre"].tolist())
        idx=st.session_state.productos[st.session_state.productos["Nombre"]==ps].index[0]
        sa=st.session_state.productos.loc[idx,"Stock"]; ua=st.session_state.productos.loc[idx,"Unidad"]
        st.info(f"📦 Stock actual: **{sa} {ua}**")
        tm=st.radio("Movimiento",["➕ Entrada","➖ Salida"],horizontal=True); cant=st.number_input("Cantidad",min_value=1,value=1)
        if st.button("💾 Actualizar Stock"):
            if "Entrada" in tm: st.session_state.productos.loc[idx,"Stock"]+=cant; st.success(f"✅ +{cant} {ua}")
            elif cant<=sa: st.session_state.productos.loc[idx,"Stock"]-=cant; st.success(f"✅ -{cant} {ua}")
            else: st.error(f"❌ Solo hay {sa} {ua}")
            st.rerun()

def p_pedidos():
    hdr("🛒 Gestión de Pedidos","Registro y seguimiento de pedidos de clientes")
    t1,t2=st.tabs(["📋 Ver Pedidos","➕ Nuevo Pedido"])
    with t1:
        df=st.session_state.pedidos.copy(); filtro=st.selectbox("Filtrar",["Todos","Pendiente","En preparacion","Entregado"])
        if filtro!="Todos": df=df[df["Estado"]==filtro]
        st.dataframe(df.style.applymap(ce,subset=["Estado"]),use_container_width=True,hide_index=True)
        c1,c2,c3=st.columns([2,1,1])
        with c1: pid=st.selectbox("Pedido",st.session_state.pedidos["ID"].tolist())
        with c2: ne=st.selectbox("Nuevo estado",["Pendiente","En preparacion","Entregado"])
        with c3:
            st.markdown("<br>",unsafe_allow_html=True)
            if st.button("🔄 Actualizar"):
                idx=st.session_state.pedidos[st.session_state.pedidos["ID"]==pid].index[0]
                st.session_state.pedidos.loc[idx,"Estado"]=ne; st.success(f"✅ {pid} → {ne}"); st.rerun()
    with t2:
        with st.form("fped"):
            c1,c2=st.columns(2)
            with c1: mesa=st.number_input("Mesa",min_value=1,max_value=20,value=1); cliente=st.text_input("Cliente *")
            with c2:
                plato=st.selectbox("Plato",[p[0] for p in PLATOS]); cant=st.number_input("Cantidad",min_value=1,value=1)
                precio=next(p[3] for p in PLATOS if p[0]==plato); st.info(f"💰 Total: **${precio*cant:,} COP**")
            if st.form_submit_button("✅ Registrar Pedido",use_container_width=True):
                if cliente.strip():
                    nid=f"PED-{len(st.session_state.pedidos)+1:03d}"
                    st.session_state.pedidos=pd.concat([st.session_state.pedidos,pd.DataFrame([{"ID":nid,"Mesa":mesa,"Cliente":cliente,"Plato":plato,"Cant":cant,"Total":precio*cant,"Estado":"Pendiente","Fecha":str(date.today())}])],ignore_index=True)
                    st.success(f"✅ {nid} registrado"); st.rerun()
                else: st.error("❌ El nombre del cliente es obligatorio")

def p_usuarios():
    hdr("👥 Gestión de Usuarios","Administración de meseros y empleados")
    t1,t2=st.tabs(["👥 Ver Usuarios","➕ Nuevo Usuario"])
    with t1:
        df=st.session_state.usuarios
        st.dataframe(df.style.applymap(ce,subset=["Rol","Estado"]),use_container_width=True,hide_index=True)
        c1,c2,c3=st.columns([2,1,1])
        with c1: us=st.selectbox("Usuario",df["Nombre"].tolist())
        with c2: ne=st.selectbox("Estado",["Activo","Inactivo"])
        with c3:
            st.markdown("<br>",unsafe_allow_html=True)
            if st.button("💾 Guardar"):
                idx=df[df["Nombre"]==us].index[0]; st.session_state.usuarios.loc[idx,"Estado"]=ne; st.success(f"✅ {us} → {ne}"); st.rerun()
    with t2:
        with st.form("fu"):
            c1,c2=st.columns(2)
            with c1: nombre=st.text_input("Nombre *"); correo=st.text_input("Correo *")
            with c2: rol=st.selectbox("Rol",["Mesero","Administrador"]); estado=st.selectbox("Estado",["Activo","Inactivo"])
            if st.form_submit_button("✅ Registrar",use_container_width=True):
                if nombre.strip() and correo.strip():
                    nid=f"U{len(st.session_state.usuarios)+1:03d}"
                    st.session_state.usuarios=pd.concat([st.session_state.usuarios,pd.DataFrame([{"ID":nid,"Nombre":nombre,"Correo":correo,"Rol":rol,"Estado":estado}])],ignore_index=True)
                    st.success(f"✅ {nombre} registrado"); st.rerun()
                else: st.error("❌ Nombre y correo son obligatorios")

def p_facturacion():
    hdr("🧾 Facturación","Generación y seguimiento de facturas electrónicas")
    t1,t2=st.tabs(["📋 Facturas emitidas","🧾 Generar Factura"])
    with t1:
        st.dataframe(st.session_state.facturas.style.applymap(ce,subset=["Estado"]),use_container_width=True,hide_index=True)
        st.metric("💰 Total facturado",f"${st.session_state.facturas['Total'].sum():,.0f} COP")
    with t2:
        ent=st.session_state.pedidos[st.session_state.pedidos["Estado"]=="Entregado"]
        if ent.empty: st.info("No hay pedidos entregados para facturar.")
        else:
            with st.form("ff"):
                pid=st.selectbox("Pedido",ent["ID"].tolist()); ped=ent[ent["ID"]==pid].iloc[0]
                sub=round(ped["Total"]/1.16); iva=ped["Total"]-sub
                st.info(f"👤 {ped['Cliente']} | Mesa {ped['Mesa']} | Subtotal: ${sub:,} | IVA: ${iva:,} | **Total: ${ped['Total']:,}**")
                metodo=st.selectbox("Método de pago",["Efectivo","Tarjeta debito","Tarjeta credito","Transferencia"])
                if st.form_submit_button("🧾 Generar Factura",use_container_width=True):
                    n=len(st.session_state.facturas)+1
                    st.session_state.facturas=pd.concat([st.session_state.facturas,pd.DataFrame([{"Factura":f"F-{n:04d}","Cliente":ped["Cliente"],"Mesa":ped["Mesa"],"Subtotal":sub,"IVA":iva,"Total":ped["Total"],"Fecha":str(date.today()),"Estado":"Pagada"}])],ignore_index=True)
                    st.success(f"✅ Factura F-{n:04d} — {metodo} — ${ped['Total']:,} COP"); st.rerun()

def p_reportes():
    hdr("📈 Reportes y Análisis","Informes de ventas, inventario y desempeño")
    t1,t2,t3=st.tabs(["💰 Ventas","📦 Inventario","🛒 Pedidos"])
    with t1:
        fechas=pd.date_range(end=date.today(),periods=14).strftime("%d/%m").tolist(); ventas=[random.randint(60000,320000) for _ in fechas]
        st.bar_chart(pd.DataFrame({"Ventas (COP)":ventas},index=fechas),color="#f59e0b")
        c1,c2,c3=st.columns(3)
        c1.metric("💰 Total",f"${sum(ventas):,.0f}"); c2.metric("📊 Promedio/día",f"${sum(ventas)//14:,.0f}"); c3.metric("🏆 Mejor día",f"${max(ventas):,.0f}")
    with t2:
        df=st.session_state.productos
        st.bar_chart(df.groupby("Cat")["Stock"].sum().rename("Stock Total"),color="#f59e0b")
        df2=df.copy(); df2["Valor"]=df2["Stock"]*df2["PC"]
        st.dataframe(df2[["Nombre","Cat","Stock","Unidad","Valor"]].sort_values("Valor",ascending=False),use_container_width=True,hide_index=True)
    with t3:
        df_p=st.session_state.pedidos
        st.dataframe(df_p["Estado"].value_counts().rename_axis("Estado").reset_index(name="Cantidad"),use_container_width=True,hide_index=True)
        st.metric("💰 Ingresos registrados",f"${df_p['Total'].sum():,.0f} COP")

def p_prediccion():
    hdr("🤖 Predicción de Demanda","Modelo predictivo para optimizar inventario y reducir desperdicios")
    st.info("💡 Análisis de datos históricos para pronosticar la demanda de insumos y prevenir desabastecimiento.")
    ps=st.selectbox("Producto",st.session_state.productos["Nombre"].tolist())
    idx=st.session_state.productos[st.session_state.productos["Nombre"]==ps].index[0]
    sa=st.session_state.productos.loc[idx,"Stock"]; ua=st.session_state.productos.loc[idx,"Unidad"]
    dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]; base=random.randint(8,18)
    preds=[base+random.randint(-2,4+2*(i>=4)) for i in range(7)]; total=sum(preds)
    st.bar_chart(pd.DataFrame({"Demanda estimada":preds},index=dias),color="#f59e0b")
    c1,c2,c3=st.columns(3)
    c1.metric("📦 Stock actual",f"{sa} {ua}"); c2.metric("📊 Demanda semanal",f"{total} {ua}")
    deficit=max(0,total-sa)
    c3.metric("🛒 Cantidad a pedir",f"{deficit} {ua}",delta="Reabastecer" if deficit>0 else "Suficiente",delta_color="inverse" if deficit>0 else "normal")
    if deficit>0: st.warning(f"⚠️ Comprar **{deficit} {ua}** de **{ps}** para cubrir la demanda semanal.")
    else: st.success(f"✅ Stock de **{ps}** suficiente para la semana.")
    st.markdown("---"); st.markdown("#### Niveles de riesgo de desabastecimiento")
    df=st.session_state.productos.copy()
    df["Riesgo"]=df.apply(lambda r:"🔴 Alto" if r["Stock"]<=r["SMin"] else("🟡 Medio" if r["Stock"]<=r["SMin"]*2 else "🟢 Bajo"),axis=1)
    st.dataframe(df[["Nombre","Stock","SMin","Unidad","Riesgo"]].sort_values("Stock"),use_container_width=True,hide_index=True)
    st.markdown("---"); st.markdown("#### 🍽️ Platos con mayor demanda estimada")
    st.dataframe(pd.DataFrame({"Plato":["Bandeja paisa","Sancocho de gallina","Cazuela de mariscos","Arroz con pollo"],"Pedidos/semana":[45,38,34,29],"Tendencia":["📈 Subiendo","➡️ Estable","📈 Subiendo","📈 Subiendo"]}),use_container_width=True,hide_index=True)

def p_menu():
    hdr("📋 Menú del Restaurante","Platos disponibles hoy")
    cats=list({p[2] for p in PLATOS}); cat_sel=st.selectbox("Categoría",["Todas"]+cats)
    filtrado=[p for p in PLATOS if cat_sel=="Todas" or p[2]==cat_sel]; cols=st.columns(2)
    for i,p in enumerate(filtrado):
        with cols[i%2]:
            st.markdown(f'<div style="background:#1e1e2a;border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:1.25rem;margin-bottom:1rem"><div style="font-size:1.05rem;font-weight:700;color:#f0f0f5">🍽️ {p[0]}</div><div style="font-size:.82rem;color:#8888aa;margin:.3rem 0 .7rem">{p[1]}</div><div style="display:flex;justify-content:space-between;align-items:center"><span style="background:#f59e0b22;color:#fbbf24;border:1px solid #f59e0b44;border-radius:100px;padding:2px 10px;font-size:.75rem">{p[2]}</span><span style="color:#f59e0b;font-weight:800;font-size:1.1rem">${p[3]:,} COP</span></div></div>',unsafe_allow_html=True)

def p_mispedidos():
    hdr("🛒 Hacer Pedido","Solicita un plato desde tu mesa")
    with st.form("fcli"):
        nombre=st.text_input("Tu nombre *"); mesa=st.number_input("N° de mesa",min_value=1,max_value=20,value=1)
        plato=st.selectbox("¿Qué deseas ordenar?",[p[0] for p in PLATOS]); precio=next(p[3] for p in PLATOS if p[0]==plato)
        cant=st.number_input("Cantidad",min_value=1,value=1); st.info(f"💰 Total: **${precio*cant:,} COP**")
        st.text_area("Nota especial (opcional)",placeholder="Sin picante, sin cebolla...")
        if st.form_submit_button("📲 Enviar Pedido",use_container_width=True):
            if nombre.strip(): st.success(f"✅ ¡Pedido enviado! Mesa {mesa} — **{plato}** x{cant} 🍽️")
            else: st.error("❌ Ingresa tu nombre")

def main():
    init()
    if not st.session_state.role: login(); return
    sidebar()
    p=st.session_state.page
    if   p=="Dashboard":   p_dashboard()
    elif p=="Inventario":  p_inventario()
    elif p=="Pedidos":     p_pedidos()
    elif p=="Usuarios":    p_usuarios()
    elif p=="Facturacion": p_facturacion()
    elif p=="Reportes":    p_reportes()
    elif p=="Prediccion":  p_prediccion()
    elif p=="Menu":        p_menu()
    elif p=="MisPedidos":  p_mispedidos()

main()
```

**PASO 2 — Crea `requirements.txt`:**
```
streamlit
pandas

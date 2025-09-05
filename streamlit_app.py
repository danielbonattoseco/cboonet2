import streamlit as st
import streamlit.components.v1 as components
import requests

# ==============================
# Configurações do Databricks
# ==============================
INSTANCE_URL = "https://adb-1450927065906591.11.azuredatabricks.net"
WORKSPACE_ID = "1450927065906591"
DASHBOARD_ID = "01f08a659f7115efb0fe2f2bab0a9eb0"

# PAT armazenado em st.secrets (não exponha no código!)
PAT = st.secrets["DATABRICKS_TOKEN"]

# ==============================
# Função para gerar embed token
# ==============================
def get_embed_token(instance_url, dashboard_id, pat):
    url = f"{instance_url}/api/2.0/aibi/dashboards/{dashboard_id}/embed-token"
    headers = {"Authorization": f"Bearer {pat}"}
    resp = requests.post(url, headers=headers)

    if resp.status_code == 200:
        return resp.json()["token"]
    else:
        st.error(f"Erro ao gerar token: {resp.text}")
        return None

# ==============================
# Gera o token de embed
# ==============================
embed_token = get_embed_token(INSTANCE_URL, DASHBOARD_ID, PAT)

if embed_token:
    # HTML com o DatabricksDashboard
    html_code = f"""
    <div id="dashboard-container" style="width:100%; height:600px;"></div>
    <script type="module">
      import {{ DatabricksDashboard }} from "https://cdn.jsdelivr.net/npm/@databricks/aibi-client/+esm";

      const dashboard = new DatabricksDashboard({{
        instanceUrl: "{INSTANCE_URL}",
        workspaceId: "{WORKSPACE_ID}",
        dashboardId: "{DASHBOARD_ID}",
        token: "{embed_token}",
        container: document.getElementById("dashboard-container"),
      }});

      dashboard.initialize();
    </script>
    """

    # Renderiza no Streamlit
    components.html(html_code, height=650)
import streamlit as st
import streamlit.components.v1 as components

# Valores do seu ambiente Databricks
instance_url = "https://adb-1450927065906591.11.azuredatabricks.net"
workspace_id = "1450927065906591"
dashboard_id = "01f08a659f7115efb0fe2f2bab0a9eb0"

# Esse token deve ser criado pelo seu backend (não hardcode!)
# Você pode usar o Databricks Personal Access Token (PAT) ou OAuth2
token = st.secrets["DATABRICKS_TOKEN"]


# HTML com o embed do DatabricksDashboard (igual ao JS, mas injetado via iframe/script)
html_code = f"""
<div id="dashboard-container" style="width:100%; height:600px;"></div>
<script type="module">
  import {{ DatabricksDashboard }} from "https://cdn.jsdelivr.net/npm/@databricks/aibi-client/+esm";

  const dashboard = new DatabricksDashboard({{
    instanceUrl: "{instance_url}",
    workspaceId: "{workspace_id}",
    dashboardId: "{dashboard_id}",
    token: "{token}",
    container: document.getElementById("dashboard-container"),
  }});

  dashboard.initialize();
</script>
"""

# Renderiza no Streamlit
components.html(html_code, height=650)
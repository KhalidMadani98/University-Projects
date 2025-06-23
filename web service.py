import os
from diagrams import Diagram, Cluster, Node
from diagrams.custom import Custom

# Set the path to the Graphviz executable
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

# Define your diagram
with Diagram("Company Services Overview", show=False, direction="LR", graph_attr={"dpi": "300", "size": "12,12"}) as diagram:
    ceo = Custom("CEO", "./icons/ceo.png")

    with Cluster("IT Department"):
        networking = Custom("Networking", "./icons/network.png")
        cybersecurity = Custom("Cybersecurity", "./icons/security.png")
        cloud = Custom("Cloud Services", "./icons/cloud.png")
        data = Custom("Data and Analytics", "./icons/data.png")
        managed = Custom("Managed Services", "./icons/managed.png")
        digital = Custom("Digital Transformation", "./icons/digital.png")
        uiux = Custom("UI/UX Design", "./icons/uiux.png")

        ceo >> networking
        ceo >> cybersecurity
        ceo >> cloud
        ceo >> data
        ceo >> managed
        ceo >> digital
        ceo >> uiux

        with Cluster("Networking"):
            nw_components = Node("Components")
            nw_processes = Node("Processes")
            nw_dependencies = Node("Dependencies")
            nw_metrics = Node("Metrics")
            networking >> nw_components
            networking >> nw_processes
            networking >> nw_dependencies
            networking >> nw_metrics

        with Cluster("Cybersecurity"):
            cs_components = Node("Components")
            cs_processes = Node("Processes")
            cs_dependencies = Node("Dependencies")
            cs_metrics = Node("Metrics")
            cybersecurity >> cs_components
            cybersecurity >> cs_processes
            cybersecurity >> cs_dependencies
            cybersecurity >> cs_metrics

        with Cluster("Cloud Services"):
            with Cluster("ServiceNow"):
                sn_components = Node("Components")
                sn_processes = Node("Processes")
                sn_dependencies = Node("Dependencies")
                sn_metrics = Node("Metrics")
                cloud >> sn_components
                cloud >> sn_processes
                cloud >> sn_dependencies
                cloud >> sn_metrics

            with Cluster("Microsoft Azure"):
                azure_components = Node("Components")
                azure_processes = Node("Processes")
                azure_dependencies = Node("Dependencies")
                azure_metrics = Node("Metrics")
                cloud >> azure_components
                cloud >> azure_processes
                cloud >> azure_dependencies
                cloud >> azure_metrics

            with Cluster("AWS"):
                aws_components = Node("Components")
                aws_processes = Node("Processes")
                aws_dependencies = Node("Dependencies")
                aws_metrics = Node("Metrics")
                cloud >> aws_components
                cloud >> aws_processes
                cloud >> aws_dependencies
                cloud >> aws_metrics

        with Cluster("Data and Analytics"):
            da_components = Node("Components")
            da_processes = Node("Processes")
            da_dependencies = Node("Dependencies")
            da_metrics = Node("Metrics")
            data >> da_components
            data >> da_processes
            data >> da_dependencies
            data >> da_metrics

        with Cluster("Managed Services"):
            ms_components = Node("Components")
            ms_processes = Node("Processes")
            ms_dependencies = Node("Dependencies")
            ms_metrics = Node("Metrics")
            managed >> ms_components
            managed >> ms_processes
            managed >> ms_dependencies
            managed >> ms_metrics

        with Cluster("Digital Transformation"):
            dt_components = Node("Components")
            dt_processes = Node("Processes")
            dt_dependencies = Node("Dependencies")
            dt_metrics = Node("Metrics")
            digital >> dt_components
            digital >> dt_processes
            digital >> dt_dependencies
            digital >> dt_metrics

        with Cluster("UI/UX Design"):
            uiux_components = Node("Components")
            uiux_processes = Node("Processes")
            uiux_dependencies = Node("Dependencies")
            uiux_metrics = Node("Metrics")
            uiux >> uiux_components
            uiux >> uiux_processes
            uiux >> uiux_dependencies
            uiux >> uiux_metrics

# Save the diagram to a file
filename = "company_services_overview"
diagram.dot.render(filename, format="png", cleanup=False)








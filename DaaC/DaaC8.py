from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.onprem.network import Tomcat
from diagrams.onprem.vcs import Github
from diagrams.generic.os import Centos, Ubuntu
from diagrams.custom import Custom
from diagrams.onprem.client import Users
from diagrams.programming.language import Java

graph_attr = {
    "fontsize": "30",
}
node_attrs = {
    "fontsize": "18",
    "fontcolor": "black",
}
edge_attrs = {
        "fontsize": "30",
}
# curvestyles = ("ortho", "curved")
# directions = ("TB", "BT", "LR", "RL")

with Diagram("GeoCitizen app ", show=True, graph_attr=graph_attr, node_attr=node_attrs, edge_attr=edge_attrs):
    dev = Custom("DevOps", "laptop.png")
    ci = Jenkins("Jenkins")
    gitt = Github("GitHub")
    ans = Ansible("Ansible")
    tera = Terraform("")
    with Cluster("VM1", graph_attr=graph_attr):
        vmu = EC2("VM Ubuntu")
        with Cluster("Ubuntu Server", graph_attr=graph_attr):
            ubun = Ubuntu("Ubuntu 20.04")
            jv = Java("Java")
            mvn = Custom("Maven", "maven.png")
            tom = Tomcat("Tomcat")
            app = Custom("GeoApp", "geoapp.png")
            ubun >> Edge(color="blue", style="bold") >> [mvn, jv, tom]
            jv << Edge(color="orange", style="dashed") >> [mvn, tom]
            mvn >> Edge(color="brown", style="bold", label="war") >> tom
            tom << Edge(color="purple", style="bold") >> app
    with Cluster("VM2", graph_attr=graph_attr):
        vmc = EC2("VM CentOS")
        with Cluster("CentOS Server", graph_attr=graph_attr):
            cent = Centos("")
            db = PostgreSQL("PostgreSQL")
            cent >> Edge(color="blue", style="bold") >> db
    dev >> Edge(color="green", style="bold") >> ci
    ci >> Edge(color="green", style="bold", label="Step 1") >> tera
    ci << Edge(color="red", style="bold", label="Response") << tera
    tera >> Edge(color="red", style="bold", label="create") >> vmc
    tera >> Edge(color="red", style="bold", label="create") >> vmu
    vmu - Edge(color="red", style="dotted") - ubun
    vmc - Edge(color="red", style="dotted") - cent
    gitt >> Edge(color="black", style="bold", label="clone") >> mvn
    ci >> Edge(color="blue", style="bold", label="Step 2") >> ans
    ans >> Edge(color="blue", style="bold", label="Install/Config") >> ubun
    ans >> Edge(color="blue", style="bold", label="Install/Config") >> cent
    Users("Users") << Edge(color="pink", style="bold") >> tom
    tom << Edge(color="purple", style="bold", label="war") >> db

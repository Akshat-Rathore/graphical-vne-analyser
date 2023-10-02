import graphviz
import hashlib
from rich import print
# Sample data for virtual nodes and links
virtual_nodes = {0: 30, 1: 45, 2: 21, 3: 82, 4: 69, 5: 52, 6: 4, 7: 88}
virtual_links = {(1, 0): [(45, 97), (97, 30)], (2, 0): [(21, 65), (65, 10), (10, 30)], (2, 1): [(21, 65), (65, 45)], (3, 0): [(82, 68), (68, 30)], (3, 1): [(82, 92), (92, 45)], (3, 2): [(82, 17), (17, 61), (61, 21)], (4, 0): [(69, 67), (67, 30)], (4, 1): [(69, 97), (97, 45)], (4, 3): [(69, 7), (7, 82)], (5, 0): [(52, 7), (7, 10), (10, 30)], (5, 1): [(52, 85), (85, 45)], (5, 2): [(52, 17), (17, 61), (61, 21)], (5, 4): [(52, 7), (7, 69)], (6, 1): [(4, 92), (92, 45)], (6, 4): [(4, 32), (32, 7), (7, 69)], (7, 0): [(88, 22), (22, 45), (45, 97), (97, 30)], (7, 2): []}

# Create a Graphviz object for the virtual graph
dot_virtual = graphviz.Digraph(comment="Virtual Network")
dot_virtual.attr(rankdir="TB")  # Top-to-bottom layout
link_mapping={}
# Add virtual nodes
for virtual_node, physical_node in virtual_nodes.items():
    dot_virtual.node(
        f"v_{virtual_node}",
        label=f"Virtual Node {virtual_node}\nPhysical Node {physical_node}",
        color="blue",
    )

for virtual_link in virtual_links:
    for link in virtual_links[virtual_link]:
        link_mapping[link]=virtual_link

# Create a function to generate unique colors based on input data
def get_unique_color(data):
    unique_hash = hashlib.sha256(data.encode()).hexdigest()
    return "#" + unique_hash[:6]  # Use the first 6 characters of the hash as an RGB color

# Create a dictionary to store unique colors for virtual links
color_mapping = {}

# Add virtual links with unique edges and consistent colors
for virtual_link, physical_links in virtual_links.items():
    virtual_link_data = str(virtual_link)
    
    # Check if the color for this virtual link has been assigned
    if virtual_link_data not in color_mapping:
        color_mapping[virtual_link_data] = get_unique_color(virtual_link_data)

    edge_color = color_mapping[virtual_link_data]
    print(edge_color,virtual_link_data)
    for physical_link in physical_links:
        physical_link_data = str(physical_link)
        # edge_label = f"Physical Link {physical_link[0]}->{physical_link[1]}"
        
        # Add virtual link with the assigned color
    dot_virtual.edge(
            f"v_{virtual_link[0]}", f"v_{virtual_link[1]}", color=edge_color
        )    
print(color_mapping)
print(link_mapping)
# Sample data for physical nodes and links
physical_nodes = set(physical_node for physical_node in virtual_nodes.values())
physical_links = set(physical_link for links in virtual_links.values() for physical_link in links)

# Create a Graphviz object for the physical graph
dot_physical = graphviz.Digraph(comment="Physical Network")
dot_physical.attr(rankdir="TB")  # Top-to-bottom layout

# Add physical nodes
for physical_node in physical_nodes:
    dot_physical.node(f"p_{physical_node}", label=f"Physical Node {physical_node}", color="red")

# Add physical links with consistent colors
for physical_link in physical_links:
    physical_link_data = str(physical_link)
    print(physical_link_data)
    edge_label = f"Physical Link {physical_link[0]}->{physical_link[1]}"
    link = link_mapping[(physical_link[0],physical_link[1])]
    edge_color = color_mapping.get(str(link))
    print(edge_color)
    dot_physical.edge(
        f"p_{physical_link[0]}", f"p_{physical_link[1]}", label=edge_label, color=edge_color
    )

# Save the graphs to files
dot_virtual.render("virtual_network", format="png")
dot_physical.render("physical_network", format="png")

class VisualMapper:
    """Step 7: Visual Mapping Module"""
    
    # Component type to shape mapping
    SHAPE_MAP = {
        # Network/Infrastructure
        'gateway': 'hexagon',
        'api gateway': 'hexagon',
        'load balancer': 'diamond',
        'balancer': 'diamond',
        'cdn': 'cloud',
        
        # Data storage
        'database': 'cylinder',
        'db': 'cylinder',
        'cache': 'cylinder',
        'storage': 'cylinder',
        'redis': 'cylinder',
        'mongodb': 'cylinder',
        'mysql': 'cylinder',
        'postgresql': 'cylinder',
        
        # Messaging
        'queue': 'parallelogram',
        'message': 'parallelogram',
        'kafka': 'parallelogram',
        'rabbitmq': 'parallelogram',
        'broker': 'parallelogram',
        
        # Services/Servers
        'service': 'rectangle',
        'server': 'rectangle',
        'microservice': 'rectangle',
        'application': 'rectangle',
        
        # Client
        'client': 'ellipse',
        'user': 'ellipse',
        'frontend': 'ellipse',
    }
    
    # Relationship type to arrow style
    ARROW_MAP = {
        'request': 'solid',
        'response': 'dashed',
        'query': 'solid',
        'write': 'solid',
        'read': 'dashed',
        'forward': 'solid',
        'route': 'solid',
        'check': 'dashed',
        'connects': 'solid',
        'sends': 'solid',
        'receives': 'dashed',
    }
    
    def map_visuals(self, normalized_data):
        """
        Map components to visual shapes and relationships to arrow styles
        """
        components = normalized_data['components']
        relationships = normalized_data['relationships']
        
        visual_components = []
        for comp in components:
            shape = self._get_shape(comp)
            color = self._get_color(comp, shape)
            
            visual_components.append({
                'name': comp,
                'shape': shape,
                'color': color
            })
        
        visual_relationships = []
        for rel in relationships:
            arrow_style = self.ARROW_MAP.get(rel['type'].lower(), 'solid')
            
            visual_relationships.append({
                'from': rel['from'],
                'to': rel['to'],
                'type': rel['type'],
                'arrow_style': arrow_style
            })
        
        return {
            'components': visual_components,
            'relationships': visual_relationships
        }
    
    def _get_shape(self, component_name):
        """
        Determine shape based on component name
        """
        name_lower = component_name.lower()
        
        for keyword, shape in self.SHAPE_MAP.items():
            if keyword in name_lower:
                return shape
        
        # Default shape
        return 'rectangle'
    
    def _get_color(self, component_name, shape):
        """
        Determine color based on component type
        """
        name_lower = component_name.lower()
        
        # Color scheme based on component type
        if shape == 'cylinder':  # Databases
            return '#4A90E2'  # Blue
        elif shape == 'hexagon':  # Gateways
            return '#7B68EE'  # Purple
        elif shape == 'diamond':  # Load Balancers
            return '#FF6B6B'  # Red
        elif shape == 'parallelogram':  # Queues
            return '#FFA500'  # Orange
        elif shape == 'ellipse':  # Clients
            return '#50C878'  # Green
        else:  # Services/Servers
            return '#95A5A6'  # Gray

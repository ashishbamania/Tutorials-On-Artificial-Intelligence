"""A Physics MCP server that implements the Model Context Protocol.
This server provides physics formulae as tools that can be discovered and used by MCP clients.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Physics-Server")

# Tool to calculate kinetic energy
@mcp.tool()
def kinetic_energy(mass: float, velocity: float) -> dict:
    """Calculate the kinetic energy of an object in motion.
    
    Formula: KE = 1/2 × mass × velocity²
    
    Args:
        mass: Mass of the object in kilograms (kg). Must be positive.
        velocity: Velocity of the object in meters per second (m/s). Can be positive or negative.
    
    Returns:
        Kinetic energy in Joules (J)
    """
    if mass <= 0:
        raise ValueError("Mass must be positive")
    
    ke = 0.5 * mass * (velocity ** 2)
    
    return ke

# Tool to calculate gravitational potential energy
@mcp.tool()
def gravitational_potential_energy(mass: float, height: float, g: float = 9.81) -> dict:
    """Calculate the gravitational potential energy of an object at a certain height.
    
    Formula: PE = mass × gravitational_acceleration × height
    
    Args:
        mass: Mass of the object in kilograms (kg). Must be positive.
        height: Height above reference point in meters (m). Must be non-negative.
        g: Gravitational acceleration in m/s². Default is 9.81 (Earth's surface).
    
    Returns:
        Gravitational potential energy in Joules (J)
    """
    if mass <= 0:
        raise ValueError("Mass must be positive")
    if height < 0:
        raise ValueError("Height must be non-negative")
    if g <= 0:
        raise ValueError("Gravitational acceleration must be positive")
    
    pe = mass * g * height
    return pe

# Tool to subtract two numbers
@mcp.tool()
def subtract(a: float, b: float) -> dict:
    """Subtract two numbers.
    
    Args:
        a: First number.    
        b: Second number.
    
    Returns:
        Difference between a and b.
    """
    return a - b

if __name__ == "__main__":
    mcp.run(transport="stdio")
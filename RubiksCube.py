class RubiksCube:
    def __init__(self):
        """
        Initialize a 3x3 Rubik's Cube with each face having the same color.
        """
        self.cube = [
            [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],  # U (Up face)
            [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],  # D (Down face)
            [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],  # F (Front face)
            [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],  # B (Back face)
            [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],  # L (Left face)
            [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],  # R (Right face)
        ]

    def display(self):
        """Display the state of the Rubik's Cube."""
        face_names = ['U', 'D', 'F', 'B', 'L', 'R']
        for i, face in enumerate(self.cube):
            print(f"{face_names[i]} Face:")
            for row in face:
                print(' '.join(row))
            print()  # Blank line after each face


# Example usage:
cube = RubiksCube()
cube.display()
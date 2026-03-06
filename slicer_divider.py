import slicer



def divide_all_lines_into_three_parts():

    """

    Divides all lines ('vtkMRMLMarkupsLineNode') found in Markups into three equal parts 

    and marks these points in the scene.

    """

    # Get all line nodes present in the scene

    lineNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsLineNode")



    if not lineNodes:

        print("No lines found in the scene. Please create lines using 'Create New Line'.")

        return



    print(f"Found {len(lineNodes)} lines in the scene. Dividing each line into three equal parts and marking them...")

    

    # Process each line node

    for lineNode in lineNodes:

        # Get the endpoints of the line

        point1 = [0.0, 0.0, 0.0]

        point2 = [0.0, 0.0, 0.0]

        lineNode.GetNthControlPointPosition(0, point1)

        lineNode.GetNthControlPointPosition(1, point2)



        # Calculate the points that divide the line into three equal parts

        firstThird = [

            point1[0] + (point2[0] - point1[0]) / 3,

            point1[1] + (point2[1] - point1[1]) / 3,

            point1[2] + (point2[2] - point1[2]) / 3

        ]

        secondThird = [

            point1[0] + 2 * (point2[0] - point1[0]) / 3,

            point1[1] + 2 * (point2[1] - point1[1]) / 3,

            point1[2] + 2 * (point2[2] - point1[2]) / 3

        ]



        # Create a fiducial node for the line

        fiducialNode = slicer.mrmlScene.AddNewNodeByClass(

            "vtkMRMLMarkupsFiducialNode", f"DividedPoints_{lineNode.GetName()}"

        )



        # Mark the 1/3 points (without using labels)

        fiducialNode.AddFiducialFromArray(point1)  # Start points

        fiducialNode.AddFiducialFromArray(firstThird)

        fiducialNode.AddFiducialFromArray(secondThird)

        fiducialNode.AddFiducialFromArray(point2)  # End points



        # Change the size and colors of the points

        displayNode = fiducialNode.GetDisplayNode()

        if displayNode:

            displayNode.SetGlyphScale(2.0)  # Increase size

            displayNode.SetSelectedColor(1.0, 0.0, 0.0)  # Set color to red (middle points)



        # Set a separate color for start and end points

        for i in [0, 3]:  # Start (0) and end (3) indices

            fiducialNode.SetNthFiducialSelected(i, True)

            fiducialNode.SetNthControlPointDescription(i, "Special")  # Label if necessary

            fiducialNode.GetDisplayNode().SetNthFiducialColor(i, 0.0, 1.0, 0.0)  # Green color



        print(f"Line '{lineNode.GetName()}' marked.")



    print("All lines successfully divided and marked.")



# Example usage

def main():

    divide_all_lines_into_three_parts()



# Run

main()
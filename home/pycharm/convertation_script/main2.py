import cv2

# Define the character map for grayscale values
char_map = {
    0: " ",
    25: ".",
    50: ":",
    75: "-",
    100: "+",
    125: "*",
    150: "%",
    175: "#",
    200: "@",
}

# Open the input video
cap = cv2.VideoCapture("input.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file!")
    exit()

# Get video properties (width, height, and FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object for the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if frame reading failed
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create the text frame (empty string)
    text_frame = ""

    # Loop through each pixel in the grayscale frame
    for i in range(height):
        for j in range(width):
            # Get the grayscale pixel value
            pixel_value = gray[i, j]

            # Look up the corresponding character in the map
            char = char_map.get(pixel_value, " ")  # Use " " if value not in map

            # Add the character to the text frame
            text_frame += char

        # Add a newline character after each row of pixels
        text_frame += "\n"

    # Print the text frame for debugging (optional)
    # print(text_frame)

    # Write the text frame to the output video
    out.write(text_frame.encode())  # Encode for video writing

# Release resources
cap.release()
out.release()

print("Video processing complete!")
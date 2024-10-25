import os
import random
import shutil
import argparse


def split_dataset(input_folder, train_ratio, val_ratio, test_ratio, seed=None):
    # Set the seed for reproducibility
    if seed is not None:
        random.seed(seed)

    # Ensure that the ratios sum up to 1
    total_ratio = train_ratio + val_ratio + test_ratio
    if abs(total_ratio - 1.0) > 1e-6:
        raise ValueError("The sum of train, val, and test ratios must be 1.")

    # Define paths for train, val, and test folders
    train_folder = os.path.join(input_folder, "train")
    val_folder = os.path.join(input_folder, "val")
    test_folder = os.path.join(input_folder, "test")

    # Create train, val, and test directories if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # List all image files in the input folder
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    images = [
        f
        for f in os.listdir(input_folder)
        if f.lower().endswith(image_extensions)
        and os.path.isfile(os.path.join(input_folder, f))
    ]

    # Shuffle the images randomly
    random.shuffle(images)

    # Calculate split indices
    total_images = len(images)
    train_end = int(total_images * train_ratio)
    val_end = train_end + int(total_images * val_ratio)

    # Split the images into train, val, and test sets
    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    # Move the images to their respective folders
    for image in train_images:
        src = os.path.join(input_folder, image)
        dst = os.path.join(train_folder, image)
        shutil.move(src, dst)

    for image in val_images:
        src = os.path.join(input_folder, image)
        dst = os.path.join(val_folder, image)
        shutil.move(src, dst)

    for image in test_images:
        src = os.path.join(input_folder, image)
        dst = os.path.join(test_folder, image)
        shutil.move(src, dst)

    print(f"Total images: {total_images}")
    print(f"Moved {len(train_images)} images to {train_folder}")
    print(f"Moved {len(val_images)} images to {val_folder}")
    print(f"Moved {len(test_images)} images to {test_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split dataset into training, validation, and testing sets."
    )
    parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        required=True,
        help="Path to the input folder containing images.",
    )
    parser.add_argument(
        "-t",
        "--train_ratio",
        type=float,
        required=True,
        help="Ratio of training set (e.g., 0.8).",
    )
    parser.add_argument(
        "-v",
        "--val_ratio",
        type=float,
        required=True,
        help="Ratio of validation set (e.g., 0.1).",
    )
    parser.add_argument(
        "-e",
        "--test_ratio",
        type=float,
        required=True,
        help="Ratio of testing set (e.g., 0.1).",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility.",
    )

    args = parser.parse_args()

    split_dataset(args.input_folder, args.train_ratio, args.val_ratio, args.test_ratio, args.seed)

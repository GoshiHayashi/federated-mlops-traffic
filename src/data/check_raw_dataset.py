from pathlib import Path

RAW_DIR = Path("datasets/raw/bdd100k")

def count_files(folder: Path, suffixes=(".jpg", ".png", ".jpeg")):
    if not folder.exists():
        return 0
    return sum(1 for p in folder.rglob("*") if p.suffix.lower() in suffixes)

def main():
    print("Checking raw dataset...")
    print("-" * 40)

    train_img_dir = RAW_DIR / "images" / "train"
    val_img_dir = RAW_DIR / "images" / "val"
    label_dir = RAW_DIR / "labels"

    print("Train images:", count_files(train_img_dir))
    print("Val images:", count_files(val_img_dir))

    print("Label files:")
    if label_dir.exists():
        for file in label_dir.iterdir():
            print(" -", file.name)
    else:
        print("No labels folder found")

if __name__ == "__main__":
    main()
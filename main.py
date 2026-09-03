from metadata import get_metadata

path = input("Enter image path: ").strip()

result = get_metadata(path)

if result is None:
    print("❌ Image not found.")
else:
    print("\n🖼️ Image Metadata")
    print("=" * 35)

    for key, value in result.items():
        print(f"{key:<12}: {value}")

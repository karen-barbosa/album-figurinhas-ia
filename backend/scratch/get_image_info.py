import struct

def get_image_size(fname):
    with open(fname, 'rb') as f:
        # Check JPEG header
        data = f.read(2)
        if data != b'\xFF\xD8':
            print("Não é um JPEG válido ou não foi possível ler o cabeçalho.")
            return None
        
        while True:
            # Read marker
            marker = f.read(2)
            if not marker:
                break
            if marker[0] != 0xFF:
                break
            # Markers SOF0 to SOF15 (except SOF4, SOF12, etc.) contain size
            if marker[1] in [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF]:
                # Read length of segment
                length = struct.unpack('>H', f.read(2))[0]
                # Read data precision (1 byte)
                f.read(1)
                # Read height and width
                height, width = struct.unpack('>HH', f.read(4))
                return width, height
            else:
                # Skip this segment
                length = struct.unpack('>H', f.read(2))[0]
                f.read(length - 2)
    return None

if __name__ == "__main__":
    path = r"c:\Users\Karen Barbosa\Downloads\backend\figurinhas\30-Karen Barbosa.jpg"
    size = get_image_size(path)
    if size:
        print(f"Dimensions of 30-Karen Barbosa.jpg: Width={size[0]}, Height={size[1]}, Ratio={size[0]/size[1]:.3f}")
    else:
        print("Não foi possível ler as dimensões.")

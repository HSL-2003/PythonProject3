import psycopg2
from config import load_config


def write_draw(part_id, path_to_file, extension):
    conn = None
    try:
        # FIX 1: Chỉ mở đúng path_to_file nếu ông đã truyền full tên file
        with open(path_to_file, 'rb') as f:
            drawing_binary = f.read()

        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Giữ nguyên bảng part_drawings
        sql = """INSERT INTO part_drawings (part_id, file_extension, draw_data) \
                 VALUES (%s, %s, %s) """
        cur.execute(sql, (part_id, extension, psycopg2.Binary(drawing_binary)))

        conn.commit()
        cur.close()
        print(f"✅ Saved drawing {part_id} to database from {path_to_file}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error in write_draw: {error}")
    finally:
        if conn:
            conn.close()


def read_drawing(part_id, path_to_save):
    params = load_config()
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # FIX 2: Phải SELECT từ bảng part_drawings, không phải từ cột draw_data
        cur.execute("SELECT draw_data FROM part_drawings WHERE part_id = %s", (part_id,))
        blob = cur.fetchone()

        if blob:
            with open(path_to_save, 'wb') as f:
                # blob[0] chứa dữ liệu nhị phân của cột draw_data
                f.write(blob[0])
                print(f" Shipped image from DB to file: {path_to_save}")
        else:
            print(f" I ain't see shit nigga! No data for ID {part_id}")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f" Error in read_drawing: {error}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Lưu ý: File 'test.png' phải có sẵn trong thư mục code
    write_draw(1, 'test.png', 'png')

    # Xuất ra file mới để kiểm tra
    read_drawing(1, 'result.png')
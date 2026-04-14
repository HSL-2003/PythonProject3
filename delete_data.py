import psycopg2
from config import load_config


def delete_part(part_id):
    """ Xóa một linh kiện dựa trên ID """
    conn = None
    rows_deleted = 0
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = "DELETE FROM part_drawings WHERE part_id = %s"

        cur.execute(sql, (part_id,))

        rows_deleted = cur.rowcount

        conn.commit()

        cur.close()
        if rows_deleted > 0:
            print(f" Đã xóa sổ hoàn toàn linh kiện ID {part_id}!")
        else:
            print(f" Không tìm thấy kẻ nào có ID {part_id} để trảm, nigga!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f" Lỗi khi thi triển chiêu thức: {error}")
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    delete_part(1)
import psycopg2


def get_count(v_id):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="Fptureset@2003")
        cur = conn.cursor()

        # Gọi hàm và lấy giá trị trả về
        cur.execute("SELECT count_vendor_parts(%s)", (v_id,))

        result = cur.fetchone()[0]
        print(f"Nhà cung cấp {v_id} có {result} linh kiện.")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_count(1)  # Thử với nhà cung cấp ID số 1
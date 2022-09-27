from main.connect_to_db import ConnectToDatabase as CD


def get_total_proportion(total_proportion, proportion):
    total_proportion += proportion
    return total_proportion


class QueryData:
    con = CD._connecting_to_db()
    cur = con.cursor()

    def get_langs_bytes(self, org):
        try:
            self.cur.execute(
                f"select language_typ, number_of_bytes from public.languages where organisation_name = '{org}' order by number_of_bytes desc")
            langs_bytes = self.cur.fetchall()
            return langs_bytes
        except Exception as e:
            print(e)
            return []

        # for lan_byte in lang_bytes:
        #    print(lan_byte)

    def get_total_bytes(self, org):
        try:
            self.cur.execute(f"select sum(number_of_bytes) from public.languages where organisation_name = '{org}'")
            total = self.cur.fetchall()
            return total[0][0]
        except Exception as e:
            print(e)
            return -1

    def get_proportion(self, langs_bytes, lang: str, total_bytes):
        if langs_bytes:
            filtered_lang_byte = list(filter(lambda lang_byte: lang_byte[0] == lang, langs_bytes))
            byte = filtered_lang_byte[0][1]
            proportion = (byte / total_bytes) * 1000
            return proportion
        else:
            print("your languages bytes table is empty")
            return -1


"""
if __name__ == "__main__":
    lang_bytes = QueryData().get_langs_bytes("facebook")
    total = QueryData().get_total_bytes("facebook")
    pro = QueryData().get_proportion( lang_bytes, "Java", total)
    print(pro)
    print(lang_bytes)
    print(total)
    otal = get_total_proportion(454.4026712710185, 454.4026712710185)
    print(otal)
"""

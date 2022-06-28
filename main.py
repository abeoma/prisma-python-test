from prisma import Prisma


def main() -> None:
    db = Prisma()
    db.connect()

    user = db.user.create(  # db.userで補完がきく！！！
        {
            "name": "Taro",
        }
    )
    print(f"created user: {user.json(indent=2, sort_keys=True)}")

    found = db.user.find_unique(where={"id": user.id})
    assert found is not None
    print(f"found user name: {found.name}")  # found.nameも補完がきく！！！

    db.disconnect()


if __name__ == "__main__":

    main()

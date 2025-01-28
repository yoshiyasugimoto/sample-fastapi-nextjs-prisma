### 起動

1. マイグレーション
   - DB テーブルを作成する

```sh
docker compose run backend prisma migrate dev
```

2. Prisma Client(型生成)

```sh
 docker compose run backend prisma generate
```

3. コンテナの起動

```sh
docker compose up
```

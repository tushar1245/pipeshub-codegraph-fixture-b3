const { reindexAll } = require("./reindex.cjs");

if (require.main === module) {
  reindexAll(process.argv.slice(2))
    .then((count) => console.log(`queued ${count} records`))
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
}

const fs = require("fs");
const csv = require("fast-csv");

fs.createReadStream(
  "./data/stack-overflow-developer-survey-2025/survey_results_public.csv"
)
  .pipe(csv.parse({ headers: true }))
  .on("data", (row) => {
    console.log("ROW TYPE:", typeof row);
    console.log(row);   // should be normal object
    process.exit();    // stop after first row
  })
  .on("error", (err) => {
    console.error("CSV ERROR:", err);
  });

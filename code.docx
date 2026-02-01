require("dotenv").config();
const mongoose = require("mongoose");
const fs = require("fs");
const csv = require("fast-csv");

const LIMIT = 5;      // change anytime
const BATCH_SIZE = 1;

async function ingestCSV() {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log("✅ MongoDB Connected");

    const schema = new mongoose.Schema({}, { strict: false });
    const Record =
      mongoose.models.survey_records ||
      mongoose.model("survey_records", schema);

    let batch = [];
    let totalInserted = 0;

    fs.createReadStream(
      "./data/stack-overflow-developer-survey-2025/survey_results_public.csv"
    )
      .pipe(csv.parse({ headers: true }))
      .on("data", async (row) => {

        batch.push(row);

        if (batch.length >= BATCH_SIZE) {
          await Record.insertMany(batch);
          totalInserted += batch.length;
          console.log("Inserted:", totalInserted);
          batch = [];
        }

        if (totalInserted >= LIMIT) {
          console.log("🎯 Limit reached");
          process.exit();
        }
      })
      .on("end", async () => {

        if (batch.length) {
          await Record.insertMany(batch);
          totalInserted += batch.length;
        }

        console.log("🚀 Done! Total:", totalInserted);
        process.exit();
      });

  } catch (err) {
    console.error("❌ Error:", err);
    process.exit(1);
  }
}

ingestCSV();

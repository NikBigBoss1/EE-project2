<template>
  <div class="flex flex-col justify-center items-center p-5 h-screen box-border">
    <header class="text-[40px] font-roboto font-light text-[#f5f5f5] mb-[5vh] text-center">
      Download Experiment Results
    </header>
    <button
      @click="downloadCSV"
      class="bg-[#01c2cd] text-[#f5f5f5] px-6 py-3 rounded-full font-roboto font-light hover:shadow-[0_0_15px_#f5f5f5] transition-shadow duration-300"
    >
      Download CSV
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const results = ref([]);

const fetchResults = async () => {
  try {
    const response = await fetch("/api/result/get");
    results.value = await response.json();
  } catch (error) {
    console.error("Error fetching results:", error);
  }
};

const convertToCSV = (data) => {
  let csvContent = "experience,gender,languageProficiency,age,type,collocation,firstGuess,time\n";
  data.forEach((entry) => {
        entry.collocations.forEach((collocation) => {
          csvContent += `${entry.experience},${entry.gender},${entry.englishProficiency},${entry.age},${collocation.type},${collocation.collocation},${collocation.firstGuess},${collocation.time}\n`;

    })
    csvContent += "\n";
  });
  return csvContent;
}

const downloadCSV = async () => {
  if (results.value.length === 0) {
    await fetchResults();
  }

  const csvContent = convertToCSV(results.value);

  // Create a Blob and download it
  const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", "experiment_results.csv");
  link.style.visibility = "hidden";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

//-------------Function to create multiple csv files.----------------
//   const downloadCSV = async () => {
//     if (results.value.length === 0) {
//       await fetchResults();
//     }
  
//     results.value.forEach((entry, index) => {
//       let csvContent = `${entry.experience},${entry.gender},${entry.englishProficiency},${entry.age}\n`;
//       entry.collocations.forEach((collocation) => {
//         csvContent += `${collocation.type},${collocation.collocation},${collocation.firstGuess},${collocation.time}\n`;
//       });
  
//       const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
//       const url = URL.createObjectURL(blob);
//       const link = document.createElement("a");
//       link.setAttribute("href", url);
//       link.setAttribute("download", `experiment_result_${index + 1}.csv`);
//       link.style.visibility = "hidden";
//       document.body.appendChild(link);
//       link.click();
//       document.body.removeChild(link);
//     });
//   };


// Fetch results initially
fetchResults();
</script>

<style scoped>
</style>
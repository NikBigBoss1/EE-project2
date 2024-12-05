<template>
    <div class="experiment-container">
      <header class="project-name">Identifier Readability</header>
  
      <div class="timer">Time Elapsed: {{ timerInSeconds }} seconds</div>
  
      <CollocationBox
        v-if="currentCollocation"
        ref="collocationBoxRef"
        :collocation="currentCollocation.collocation"
        :choices="currentCollocation.choices"
        :type="currentCollocation.type"
        @correctChoiceSelected="onCorrectChoice"
      />
  
      <div v-if="showThankYouMessage">
        <p>Thank you for your time!</p>
        <NuxtLink 
            to="/" 
            class="next-button"
        >   Finish
        </NuxtLink>
      </div>

      <button
        v-if="showNextButton"
        class="next-button"
        @click="goToNextCollocation"
      >
        Next
      </button>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, computed } from "vue";
import CollocationBox from "~/components/CollocationBox.vue";

import { useWebsiteStore } from '~/store/website';
const websiteStore = useWebsiteStore();

const collocations = ref([]);
const currentIndex = ref(0);
const showNextButton = ref(false);

const timerInSeconds = ref(0);
const timerInMilliseconds = ref(0);

let timerIntervalInSeconds = null;
let timerIntervalInMilliseconds = null;

const collocationBoxRef = ref(null); // Reference to CollocationBox component
const showThankYouMessage = ref(false);


const fetchCollocations = async () => {
  const response = await fetch("/api/collocations/get");
  const data = await response.json();
  collocations.value = data;
};

// Start and stop timer in seconds and milliseconds
const startTimerInSeconds = () => {
    timerInSeconds.value = 0;
    timerIntervalInSeconds = setInterval(() => {
    timerInSeconds.value++;
  }, 1000);
};
const stopTimerInSeconds = () => {
  clearInterval(timerIntervalInSeconds);
};

const startTimerInMilliseconds = () => {
    timerInMilliseconds.value = 0;
    timerIntervalInMilliseconds = setInterval(() => {
    timerInMilliseconds.value++;
  }, 1);
};
const stopTimerInMilliseconds = () => {
  clearInterval(timerIntervalInMilliseconds);
};
//////////////////////////////////////////


const goToNextCollocation = () => {
  if (currentIndex.value < collocations.value.length - 1) {
    collocationBoxRef.value?.resetFirstGuess();
    currentIndex.value++;
    showNextButton.value = false;
    startTimerInSeconds();
    startTimerInMilliseconds();
   }
};

const currentCollocation = computed(() => collocations.value[currentIndex.value]);

const onCorrectChoice = (firstGuess) => {
  stopTimerInMilliseconds();
  stopTimerInSeconds();

  // Save the current collocation result
  websiteStore.collocations.push({
    type: currentCollocation.value.type,
    collocation: currentCollocation.value.collocation,
    firstGuess,
    time: timerInMilliseconds.value,
  });

  if (currentIndex.value === collocations.value.length - 1) {
    saveResultToDB();
    showThankYouMessage.value = true;
  } else {
    showNextButton.value = true;
  }
};


const saveResultToDB = async () => {
  const resultData = {
    ...websiteStore.form,
    collocations: websiteStore.collocations,
  };

  const response = await fetch('/api/result/saveResult', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(resultData),
  });

  const result = await response.json();
  if (result.success) {
    console.log('Experiment data saved successfully:');
  } else {
    console.error('Error saving experiment data:', result.error);
  }
};

onMounted(() => {
  fetchCollocations().then(() => {
    startTimerInSeconds();
    startTimerInMilliseconds();
  });
});
</script>
  






<style scoped>
/* Experiment name styling */
.project-name {
  font-size: 40px;
  font-weight: 600;
  font-family: 'Griffy', sans-serif;
  color: #333;
  margin-bottom: 5vh;
  text-align: center;
}
.experiment-container {
  text-align: center;
  padding: 20px;
}

.experiment-name {
  font-size: 2rem;
  margin-bottom: 20px;
}

.timer {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #333;
}

/* Choice Box Styling */
.choice-box {
  margin: 10px;
  padding: 20px;
  border: 2px solid #ddd;
  border-radius: 5px;
  width: 150px;
  height: 100px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #f9f9f9;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
  color: #333;
  transition: border-color 0.1s ease;
}

.choice-box.correct {
  border-color: green;
  background-color: #e6ffe6;
}

.choice-box.incorrect {
  border-color: red;
  background-color: #ffe6e6;
}

/* Next Button Styling */
.next-button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007acc;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.next-button:hover {
  background-color: #005fa3;
}

.next-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
  </style>
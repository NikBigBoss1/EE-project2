<template>
  <div class="flex flex-col justify-center items-center p-5 min-h-screen box-border">
    <Header />

    <!-- Loading Window -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center">
        <p class="text-center text-[#f5f5f5] text-[40px] font-roboto mb-4">Loading, please wait...</p>
        <div class="spinner border-t-[#01c2cd] border-4 border-solid rounded-full h-16 w-16 animate-spin"></div>
    </div>

    <div class="flex flex-col items-center" v-if="showCollocationBox">
      <transition name="slide-fade">
        <div class="w-full max-w-lg bg-[#f5f5f5] rounded-full h-4 mb-6">
          <div class="bg-[#01c2cd] h-4 rounded-full transition-all duration-300"
            :style="{ width: progressPercentage + '%' }"></div>
        </div>
      </transition>

      <transition name="slide-fade">
        <CollocationBox ref="collocationBoxRef" :collocation="currentCollocation?.collocation"
          :choices="currentCollocation?.choices" :type="currentCollocation?.type"
          @correctChoiceSelected="onCorrectChoice" />

      </transition>

      <transition name="slide-fade">
        <div class="text-[20px] font-roboto text-[#f5f5f5] pt-8">
          Time Elapsed: {{ timerInSeconds }} seconds
        </div>
      </transition>
    </div>

    <transition name="fade">
      <div v-if="showThankYouMessage" class="text-center mt-10 flex flex-col items-center">
        <p class="text-[20px] font-roboto text-[#f5f5f5] pb-10">
          Thank you for your time!
        </p>
        <NuxtLink to="/"
          class="bg-[#01c2cd] text-[#f5f5f5] px-6 py-3 rounded-full font-roboto font-light hover:shadow-[0_0_15px_#f5f5f5] transition-shadow duration-300">
          Finish
        </NuxtLink>
      </div>
    </transition>

    <div class=" mt-8 h-12">
      <button v-if="showNextButton"
        class="bg-[#01c2cd] text-[#f5f5f5] px-6 py-3 rounded-full font-roboto font-light hover:shadow-[0_0_15px_#f5f5f5] transition-shadow duration-300"
        @click="goToNextCollocation">
        Next
      </button>
    </div>

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
const showCollocationBox = ref(true);
const isLoading = ref(true);


const fetchCollocations = async () => {
  isLoading.value = true;
  showCollocationBox.value = false;
  const response = await fetch("/api/collocations/get");
  const data = await response.json();
  collocations.value = data;
  isLoading.value = false;
  showCollocationBox.value = true;
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

const progressPercentage = computed(() => {
  if (collocations.value.length === 0) return 0;

  if (currentIndex.value === collocations.value.length - 1 && showThankYouMessage.value) {
    return 100;
  }

  return ((currentIndex.value + (showNextButton.value ? 1 : 0)) / collocations.value.length) * 100;
});
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
    setTimeout(() => {
      showCollocationBox.value = false;
      showThankYouMessage.value = true;
    }, 1000);
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
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: opacity 2s ease, transform 2s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
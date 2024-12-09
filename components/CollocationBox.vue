<template>
  <div>
    <h2 class="text-[24px] font-roboto text-[#f5f5f5] text-center pb-4">{{ collocation }}</h2>

    <div class="flex flex-wrap justify-center gap-10 mt-5">
      <div
        v-for="(choice, index) in choices"
        :key="index"
        class="flex items-center justify-center w-[150px] h-[100px] rounded-lg bg-[#f9f9f9] cursor-pointer text-[#333] font-roboto font-bold text-[16px] transition-transform transform hover:scale-105"
        :class="{ 
          'shadow-[0_0_15px_5px_green] bg-[#e6ffe6] animate-zoom': isCorrect(choice), 
          'animate-rotate-shake': isIncorrect(choice),
          'pointer-events-none': isCorrectSelected 
        }"
        @click="handleChoiceClick(choice, $event)"
      >
        {{ choice }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { defineEmits } from 'vue'

const emit = defineEmits(['correctChoiceSelected']);

const props = defineProps({
  collocation: {
    type: String,
    required: true,
  },
  choices: {
    type: Array,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
});

const firstGuess = ref(null);

const selectedIncorrectChoice = ref(null);
const selectedCorrectChoice = ref(null);
const isCorrectSelected = ref(false);

const isCorrect = (choice) => {
  return selectedCorrectChoice.value === choice;
};
const isIncorrect = (choice) => {
  return selectedIncorrectChoice.value === choice;
};

function resetFirstGuess() {
  firstGuess.value = null;
  isCorrectSelected.value = false;
}

defineExpose({
  resetFirstGuess,
});


// Utility functions to normalize the collocation string
const toCamelCase = (str) => {
  return str
    .split(" ")
    .map((word, index) =>
      index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    )
    .join("");
};

const toKebabCase = (str) => {
  return str.split(" ").join("-").toLowerCase();
};

const normalizeCollocation = () => {
  if (props.type === "camelCase") {
    return toCamelCase(props.collocation);
  } else if (props.type === "kebab-case") {
    return toKebabCase(props.collocation);
  }
  return props.collocation;
};
////////////////////////////////////


const handleChoiceClick = (choice, event) => {
  const normalizedCollocation = normalizeCollocation();
  if (firstGuess.value === null) {
    firstGuess.value = choice === normalizedCollocation;
  }

  if (choice === normalizedCollocation) {
    selectedCorrectChoice.value = choice;
    isCorrectSelected.value = true;
    event.target.classList.add("correct");
    emit("correctChoiceSelected", firstGuess.value);
  } else {
    selectedIncorrectChoice.value = choice;
    event.target.classList.add("incorrect");
    setTimeout(() => {
      event.target.classList.remove("incorrect");
    }, 100);
  }
};
</script>



<style scoped> 

@keyframes zoom {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
}

@keyframes glow-shake {
  0%, 100% {
    transform: rotate(0deg);
    box-shadow: 0 0 0 0 red; /* No glow at the start and end */
  }
  25%, 75% {
    transform: rotate(-10deg);
    box-shadow: 0 0 15px 5px red; 
    background-color: #ffe6e6;/* Red glow during shake */
  }
  50% {
    transform: rotate(10deg);
    box-shadow: 0 0 15px 5px red;
    background-color: #ffe6e6; /* Red glow during shake */
  }
}

.animate-zoom {
  animation: zoom 500ms ease-in-out;
}

.animate-rotate-shake {
  animation: glow-shake 500ms ease;
}
</style>

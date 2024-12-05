<template>
    <div>

      <h2>{{ collocation }}</h2>
      
      <div class="collocation-boxes">
        <div
          v-for="(choice, index) in choices"
          :key="index"
          class="choice-box"
          :class="{ correct: isCorrect(choice), incorrect: isIncorrect(choice) }"
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

const isCorrect = (choice) => {
  return selectedCorrectChoice.value === choice;
};
const isIncorrect = (choice) => {
  return selectedIncorrectChoice.value === choice;
};

function resetFirstGuess() {
  firstGuess.value = null;
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
.collocation-boxes {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.choice-box {
  margin: 10px;
  padding: 20px;
  border: 2px solid #ddd;
  border-radius: 5px;
  width: 150px;
  height: 100px;
  display: flex;
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
</style>
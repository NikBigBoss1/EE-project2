<template>
  <div class="page-container">
    <header class="project-name">Identifier Readability</header>

    <form class="questionnaire-form">
      <div class="form-group">
        <label for="experience">Experience:</label>
        <select id="experience" v-model="form.experience" required>
          <option value="">Select your experience</option>
          <option value="less than one year">Less than one year</option>
          <option value="one to three years">One to three years</option>
          <option value="more than three years">More than three years</option>
        </select>
      </div>

      <div class="form-group">
        <label for="gender">Gender:</label>
        <div>
          <label>
            <input
              type="radio"
              value="male"
              v-model="form.gender"
              required
            />
            Male
          </label>
          <label>
            <input
              type="radio"
              value="female"
              v-model="form.gender"
              required
            />
            Female
          </label>
        </div>
      </div>
      <div class="form-group">
        <label for="englishProficiency">English Proficiency:</label>
        <select id="englishProficiency" v-model="form.englishProficiency" required>
          <option value="">Select your English proficiency</option>
          <option value="native speaker">Native Speaker</option>
          <option value="second language">Second Language (Fluent or near-fluent)</option>
          <option value="foreign language">Foreign Language (Basic or moderate proficiency)</option>
        </select>
      </div>

      <div class="form-group">
        <label for="age">Age:</label>
        <input
          type="number"
          id="age"
          v-model="form.age"
          min="1"
          max="120"
          required
          placeholder="Enter your age"
        />
      </div>
    </form>
    <div class="instruction-text">
      <p>After you click the "Start Experiment" button, the calculation will begin immediately.</p>
    </div>
    <div class="button-container">
      <NuxtLink
        v-if="isFormValid"
        to="/experiment"
        class="start-button"
        @click.prevent="submitForm"
      >
        Start Experiment
      </NuxtLink>
    </div>
  </div>
</template>


<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useWebsiteStore } from '~/store/website';
const websiteStore = useWebsiteStore();

const router = useRouter();

// Bind the store's form to the template
const form = computed(() => websiteStore.form);

const isFormValid = computed(() => {
  return (
    form.value?.experience &&
    form.value?.gender &&
    form.value?.age &&
    form.value?.englishProficiency
  );
});

async function submitForm() {
  // Store form data in the store
  websiteStore.setFormData(form.value);
  router.push('/experiment');
}
</script>
  



<style scoped>
/* General page styling */
.page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  min-height: 100vh;
  box-sizing: border-box;
}

/* Experiment name styling */
.project-name {
  font-size: 40px;
  font-weight: 600;
  font-family: 'Griffy', sans-serif;
  color: #333;
  margin-bottom: 5vh;
  text-align: center;
}

/* Form styling */
.questionnaire-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  max-width: 600px;
  background: #fff;
  padding: 20px;
  padding-bottom: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Form groups */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-weight: bold;
  font-family: 'Roboto Flex', sans-serif;
  color: #333;
}

input,
select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  font-family: 'Roboto Flex', sans-serif;
}

/* Button styling */
.button-container {
  display: flex;
  justify-content: center;
}

.start-button {
  display: inline-block;
  background-color: #007acc;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.start-button:hover {
  background-color: #005fa3;
}

.start-button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}
</style>
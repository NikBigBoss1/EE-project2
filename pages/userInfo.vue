<template>
  <div class="flex flex-col justify-center items-center p-5 min-h-screen box-border">
   <Header />

    <div class="grid grid-cols-2 gap-10 w-full max-w-[800px]">
      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">Experience</h6>
        <select
          id="experience"
          v-model="form.experience"
          class="w-full px-3 py-2 border rounded-md text-[15px] font-roboto  dark:text-[#f5f5f5] placeholder:dark:text-[#0d0d0d]"
          required
        >
          <option value="">Select your experience</option>
          <option value="less than one year">Less than one year</option>
          <option value="one to three years">One to three years</option>
          <option value="more than three years">More than three years</option>
        </select>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">Gender</h6>
        <div class="flex space-x-4">
          <label class="font-roboto text-[15px] text-[#0d0d0d]">
            <input
              type="radio"
              value="male"
              v-model="form.gender"
              required
              class="mr-2"
            />
            Male
          </label>
          <label class="font-roboto text-[15px] text-[#0d0d0d]">
            <input
              type="radio"
              value="female"
              v-model="form.gender"
              required
              class="mr-2"
            />
            Female
          </label>
        </div>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">
          English Proficiency
        </h6>
        <select
          id="englishProficiency"
          v-model="form.englishProficiency"
          class="w-full px-3 py-2 border rounded-md text-[15px] font-roboto  dark:text-[#f5f5f5] placeholder:dark:text-[#0d0d0d]"
          required
        >
          <option value="">Select your English proficiency</option>
          <option value="native speaker">Native Speaker</option>
          <option value="second language">Second Language (Fluent or near-fluent)</option>
          <option value="foreign language">Foreign Language (Basic or moderate proficiency)</option>
        </select>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">Age</h6>
        <input
          type="number"
          id="age"
          v-model="form.age"
          min="1"
          max="120"
          required
          placeholder="Enter your age"
          class="w-full px-3 py-2 border rounded-md text-[15px] font-roboto  dark:text-[#f5f5f5] placeholder:dark:text-[#f5f5f5] placeholder-[#0d0d0d]"
        />
      </div>
    </div>

    <div class=" p-14 font-roboto font-light text-[15px] text-[#f5f5f5]">
      <p>After you click the "Start Experiment" button, the calculation will begin immediately.</p>
    </div>

    <div class="text-center">
      <NuxtLink
        to="/experiment"
        class="bg-[#01c2cd] text-[#f5f5f5] px-6 py-3 rounded-full font-roboto font-light hover:shadow-[0_0_15px_#f5f5f5] transition-shadow duration-300"
        :class="{ 'opacity-50 pointer-events-none': !isFormValid }"
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
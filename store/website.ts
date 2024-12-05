import { defineStore } from 'pinia';
import { ref } from 'vue';

interface Form {
  experience: string;
  gender: string;
  age: number | null;
  englishProficiency: string;
}

export const useWebsiteStore = defineStore('website', () => {
  const form = ref<Form>({
    experience: '',
    gender: '',
    age: null,
    englishProficiency: '',
  });

  // Dynamically build collocations during the experiment
  const collocations = ref<Array<{
    type: string;
    collocation: string;
    firstGuess: boolean;
    time: number;
  }>>([]);

  const setFormData = (newForm: Form) => {
    form.value = { ...newForm };
  };

  return { form, collocations, setFormData };
});
<template>
  <div class="flex flex-col justify-center items-center p-5 min-h-screen box-border">
    <Header  :hasAnimation="true" />

    <div class="grid grid-cols-2 gap-10 w-full max-w-[800px]">
      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">
          Purpose
        </h6>
        <p class="font-roboto text-[15px] text-[#0d0d0d]">
          Help us explore if camelCase or kebab-case is easier to read in programming.
        </p>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <p class="font-roboto text-[20px] text-[#0d0d0d] pb-3">Your Task:</p>
        <ul class="font-roboto text-[16px] text-[#0d0d0d] list-disc list-inside">
          <li>View a short sentence.</li>
          <li>Select the matching identifier from a list.</li>
          <li>Repeat for several examples in both styles.</li>
        </ul>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">
          What We Measure
        </h6>
        <p class="font-roboto text-[15px] text-[#0d0d0d]">
          Your accuracy and response time.
        </p>
      </div>

      <div class="bg-[#f5f5f5] p-5 rounded-lg shadow-[0_0_15px_#f5f5f5] min-h-[100px]">
        <h6 class="font-roboto text-[20px] text-[#0d0d0d] pb-3">
          How to Start
        </h6>
        <p class="font-roboto text-[15px] text-[#0d0d0d]">
          Fill in a quick demographics form and follow the on-screen instructions.
        </p>
      </div>
    </div>
    <div class="text-center mt-16">
      <NuxtLink to="/userInfo"
        class="bg-[#01c2cd] text-[#f5f5f5] px-6 py-3 rounded-full font-roboto font-light hover:shadow-[0_0_15px_#f5f5f5] transition-shadow duration-300">
        Start Experiment
      </NuxtLink>
    </div>

  </div>
</template>



<script setup>
</script>


<style scoped></style>
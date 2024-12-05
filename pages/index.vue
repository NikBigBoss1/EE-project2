<template>
    <div class="page-container">
      <header class="project-name">Identifier Readability</header>
  
      <div class="cards-container">
        <div class="card">
          <p class="card-text">
            Card 1: Clear instructions are provided for the participants.
          </p>
        </div>
        <div class="card">
          <p class="card-text">
            Card 2: Explains the goal of the experiment.
          </p>
        </div>
        <div class="card">
          <p class="card-text">
            Card 3: Describes what participants are supposed to do.
          </p>
        </div>
        <div class="card">
          <p class="card-text">
            Card 4: Additional notes or tips for the experiment.
          </p>
        </div>
      </div>
  
      <div class="button-container">
        <NuxtLink to="/userInfo" class="start-button">Start Experiment</NuxtLink>
      </div>

    </div>
  </template>
  
  <script setup>
  </script>
  
  
  <style scoped>
  /* General page styling */
  .page-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    height: 100vh;
    box-sizing: border-box;
  }
  
  /* Project Name styling */
  .project-name {
    font-size: 40px;
    font-weight: 600;
    font-family: 'Griffy', sans-serif;
    color: #333;
    margin-bottom: 5vh;
    text-align: center;
  }
  
  /* Cards container styling */
  .cards-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* Two cards per row */
    gap: 20px; /* Space between cards */
    width: 100%;
    max-width: 800px; /* Ensures the grid doesn't stretch too wide */
  }
  
  /* Individual card styling */
  .card {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .card-text {
    font-size: 16px;
    font-family: 'Roboto Flex', sans-serif;
    color: #555;
  }
  
  /* Button styling */
  .button-container {
    text-align: center;
    margin-top: 20px;
  }
  
  .start-button {
    background-color: #007acc;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .start-button:hover {
    background-color: #005fa3; /* Darker blue on hover */
  }
  </style>
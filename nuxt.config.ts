// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  components: true,
  app: {
    head: {
      title: 'EE-project 2',
     charset: 'utf-8',
     viewport: 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0, viewport-fit=cover',
      meta: [
        {name: 'color-scheme', content: 'light dark'},
      ],

    }
  },
  modules: [
    "@nuxtjs/google-fonts",
    '@pinia/nuxt',
    'nuxt-icon',
    'nuxt-mongoose',
  ],
  css: ['~/styles/normalize.css'],
  googleFonts: {
    families: {
      'Roboto+Flex': true,
      'Griffy': true,
    }
  },
  mongoose: {
    uri: 'mongodb://localhost:27017/',
    options: {},
    modelsDir: 'models',
    devtools: true,
  },
})

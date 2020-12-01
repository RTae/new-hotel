<template>
  <v-app id="App">
    <HeaderCore/>
    <Content/>
  </v-app>
</template>

<script>
import HeaderCore from './components/core/Header';
import Content from './components/core/Content'

export default {
  name: 'App',

  components: {
    HeaderCore,
    Content
  },

  data: () => ({
    //
  }),
};
</script>

<template>
  <v-app id="App">
    <HeaderLogin v-if="$store.getters.getHeaderLoginState"/>
    <HeaderAdmin v-if="$store.getters.getHeaderAdminState"/>
    <HeaderCore v-if="$store.getters.getHeaderCoreState"/>
    <Content/>
  </v-app>
</template>

<script>
import HeaderCore from './components/core/Header';
import Content from './components/core/Content';
import HeaderLogin from './components/core/HeaderLogin';
import HeaderAdmin from './components/core/HeaderAdmin';

export default {
  name: 'App',
  components: {
    HeaderCore,
    HeaderLogin,
    HeaderAdmin,
    Content,
  },
  mounted() {
    this.$store.dispatch({type:"restoreLogin"})
  },
};
</script>

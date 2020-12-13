<template>
  <v-app id="App">
    <HeaderCore v-if="$store.getters.getCoreHeader"/>
    <Content/>
    <Footer/>
    <HeaderLogin v-if="$store.getters.getLoginHeaderUser"/>
    <HeaderAdmin v-if="$store.getters.getLoginHeaderAdmin"/>
    <HeaderLogo v-if="$store.getters.getLogoHeader"/>
    
  </v-app>
</template>

<script>
import HeaderCore from './components/core/Header';
import Content from './components/core/Content';
import Footer from './components/core/Footer';
import HeaderLogin from './components/core/HeaderLogin';
import HeaderAdmin from './components/core/HeaderAdmin';
import HeaderLogo from './components/core/HeaderLogo';

export default {
  name: 'App',
  components: {
    HeaderCore,
    Content,
    Footer,
    HeaderLogin,
    HeaderAdmin,
    HeaderLogo
  },

  data: () => ({
    //
  }),
};
</script>

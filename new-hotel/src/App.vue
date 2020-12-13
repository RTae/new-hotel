<template>
  <v-app id="App">
    <HeaderLogin v-if="false"/>
    <HeaderAdmin v-if="true"/>
    <HeaderLogo v-if="false"/>
    <HeaderCore v-if="false"/>
    <Content/>
    <Footer/>
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
};
</script>

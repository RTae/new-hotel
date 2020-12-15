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
import HeaderLogin from './components/core/HeaderLogin';
import HeaderAdmin from './components/core/HeaderAdmin';
import HeaderLogo from './components/core/HeaderLogo';
import Footer from './components/core/Footer';

export default {
  name: 'App',
  components: {
    HeaderCore,
    Content,
    HeaderLogin,
    HeaderAdmin,
    HeaderLogo,
    Footer
  },
};
</script>

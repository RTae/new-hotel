<template>
  <div id="footer">
    <v-footer dark padless>
      <v-card class="flex" flat tile>
        <v-card-text class="text-center" cols="12">
          {{ new Date().getFullYear() }} — <strong>New Hotel</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "Footer",
};

</script>

<style>
  .footer {
      display:flex;    
      align-items:flex-end;
  }
</style>
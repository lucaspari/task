<template>
  <v-container
    class="d-flex justify-center align-center"
    style="height: 100vh;"
  >
    <v-card class="pa-5">
      <v-card-title>User Details</v-card-title>
      <v-card-text>
        <span><b>Username:</b></span><p>{{ username }}</p>
        <span><b>Active:</b></span><p>{{ active }}</p>
        <span><b>Preferences</b></span><p>{{ preferences }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "User",
  onMounted() {
    console.log("User details mounted");

  },
  data() {
    return {
      username : this.$route.params.username,
      active: this.$route.query.active,
      preferences: this.$route.query.preferences,
    };
  },
};
</script>

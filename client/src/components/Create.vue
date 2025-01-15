<template>
  <v-dialog
    v-model="localDialog"
    max-width="500px"
  >
    <v-card>
      <v-card-title class="text-h5">
        Create User
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="user.username"
                label="username"
              />
            </v-col>
            <v-col
              cols="6"
              md="6"
              sm="6"
            >
              <v-checkbox
                v-model="user.active"
                label="active"
              />
            </v-col>
          </v-row>
          <v-row
            align="center"
            justify="center"
          >
            <v-col
              cols="6"
              align="center"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="user.preferences"
                label="timezone"
              />
            </v-col>
            <v-col
              cols="6"
              align="center"
              md="6"
              sm="6"
            >
              <v-text-field
                v-model="user.password"
                type="password"
                label="password"
              />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="4">
              <v-checkbox
                v-model="isTester"
                label="tester"
              />
            </v-col>
            <v-col cols="4">
              <v-checkbox
                v-model="isAdmin"
                label="admin"
              />
            </v-col>
            <v-col cols="4">
              <v-checkbox
                v-model="isManager"
                label="manager"
              />
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer />
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="close"
            >
              Cancel
            </v-btn>
            <v-btn
              @click="save"
              color="blue-darken-1"
              variant="text"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
export default {
  name : "CreateDialog",
  props:{
    dialog: {
      type: Boolean,
      required: true
    },
  },
  emits: ['update:dialog', 'create', ],
  data() {
    return {
      localDialog: false,
      isAdmin : false,
      isManager: false,
      isTester : false,
      user: {
        username: '',
        active: false,
        preferences: '',
        password: '',
        roles : [] as string[],
        createAt: new Date(),
      }
    };
  },
  watch: {
    isAdmin(){
      if(this.isAdmin){
        this.user.roles.push('admin');
      }
      else{
        this.user.roles = this.user.roles.filter(role => role !== 'admin');
      }
    },
    isManager(){
      if(this.isManager){
        this.user.roles.push('manager');
      }
      else{
        this.user.roles = this.user.roles.filter(role => role !== 'manager');
      }
    },
    isTester(){
      if(this.isTester){
        this.user.roles.push('tester');
      }
      else{
        this.user.roles = this.user.roles.filter(role => role !== 'tester');
      }
    },
    dialog(val) {
      this.localDialog = val;
    },
    localDialog(val) {
      this.$emit('update:dialog', val);
    },
  },
  methods: {
    close() {
      this.$emit('update:dialog', false);
    },
    save(){
      this.$emit('update:dialog', false);
      this.$emit('create', this.user);
    }
  }
};
</script>

<style scoped>
</style>

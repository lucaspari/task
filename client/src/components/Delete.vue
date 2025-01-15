<template>
  <v-dialog
    v-model="localDialogDelete"
    max-width="500px"
  >
    <v-card>
      <v-card-title class="text-h5">
        Are you sure you want to delete this item?
      </v-card-title>
      <v-card-actions>
        <v-spacer />
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="closeDelete"
        >
          Cancel
        </v-btn>
        <v-btn
          color="blue-darken-1"
          variant="text"
          @click="deleteItemConfirm"
        >
          OK
        </v-btn>
        <v-spacer />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
export default {
  name: 'DeleteDialog',
  props: {
    dialogDelete: {
      type: Boolean,
      required: true
    }
  },
emits: ['update:dialogDelete', 'delete-confirm'],
data() {
  return {
    localDialogDelete: this.dialogDelete
  };
},
watch: {
  dialogDelete(val) {
    this.localDialogDelete = val;
  },
  localDialogDelete(val) {
    this.$emit('update:dialogDelete', val);
  }
},
  methods: {
    closeDelete() {
      this.$emit('update:dialogDelete', false);
    },
    deleteItemConfirm() {
      this.$emit('delete-confirm');
      this.closeDelete();
    }
  }
};
</script>

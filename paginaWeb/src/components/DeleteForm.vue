<template>
  <div>
    <h2>Eliminar Cliente</h2>
    <form class="row g-3" @submit.prevent="eliminarCliente">
      <div >
        <div >
          <label for="userId" class="form-label">ID del Cliente</label>
          <input type="number" class="form-control" v-model="userId" placeholder="123" required>
        </div>
      </div>
      <button type="submit" class="btn btn-danger mt-3">Eliminar Cliente</button>
    </form>
    <div v-if="deleteSuccess" class="alert alert-success mt-3" role="alert">
      Cliente eliminado correctamente.
    </div>
    <div v-if="deleteError" class="alert alert-danger mt-3" role="alert">
      Hubo un error al eliminar el cliente.
    </div>
  </div>
</template>

  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      userId: '',
      deleteSuccess: false,
      deleteError: false
    };
  },
  methods: {
    eliminarCliente() {
      const payload = {
        id: this.userId
      };

      axios.delete('http://127.0.0.1:5000/delete', { data: payload })
        .then(response => {
          console.log('Cliente eliminado:', response.data);
          this.deleteSuccess = true;
          this.deleteError = false;
          // Limpiar el campo de entrada después de la eliminación exitosa
          this.userId = '';
        })
        .catch(error => {
          console.error('Hubo un error al eliminar el cliente:', error);
          this.deleteSuccess = false;
          this.deleteError = true;
        });
    }
  }
};
</script>
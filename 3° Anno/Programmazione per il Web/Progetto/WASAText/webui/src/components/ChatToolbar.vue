<script>
export default {
    props: {
        isGroup: { type: Boolean, default: false },
        loading: { type: Boolean, default: false }
    },
    // Gli emit events che questo componente può emettere
    emits: ['leave', 'delete', 'set-group-name', 'set-group-photo', 'set-group-desc']
}
</script>

<template>
    <div class="d-flex align-items-center gap-2">
        
        <template v-if="isGroup">
            <button class="btn btn-sm btn-outline-primary d-flex align-items-center gap-1" @click="$emit('set-group-name')" :disabled="loading" title="Cambia Nome">
                ✏️ <span class="d-none d-md-inline">Nome</span>
            </button>

            <button class="btn btn-sm btn-outline-primary d-flex align-items-center gap-1" @click="$emit('set-group-photo')" :disabled="loading" title="Cambia Foto">
                🖼️ <span class="d-none d-md-inline">Foto</span>
            </button>

            <button class="btn btn-sm btn-outline-primary d-flex align-items-center gap-1" @click="$emit('set-group-desc')" :disabled="loading" title="Cambia Descrizione">
                📝 <span class="d-none d-md-inline">Info</span>
            </button>
            
            <div class="vr mx-1"></div>
        </template>

        <button v-if="isGroup" class="btn btn-sm btn-outline-warning" @click="$emit('leave')" :disabled="loading" title="Lascia Gruppo">
            🏃‍♂️ <span class="d-none d-md-inline">Lascia</span>
        </button>

        <button class="btn btn-sm btn-outline-danger" @click="$emit('delete')" :disabled="loading" title="Elimina">
            🗑️ <span class="d-none d-md-inline">Elimina</span>
        </button>
    </div>
</template>
<script>
export default {
    props: {
        loading: { type: Boolean, default: false },
        variant: { type: String, default: 'primary' }, 
        disabled: { type: Boolean, default: false }
    }
}
</script>

<template>
    <button 
        class="btn d-flex align-items-center justify-content-center gap-2" 
        :class="'btn-' + variant" 
        :disabled="disabled || loading"
    >
        <div v-if="loading" class="spinner-border spinner-border-sm" role="status"></div>
        
        <slot></slot>
    </button>
</template>

<style scoped>
.btn { transition: all 0.2s; font-weight: 500; }
.btn:active { transform: scale(0.98); }
</style>
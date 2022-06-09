<template>
	<div class="">
		<header-vue />
		<b-card class="mx-auto w-25 mt-3" title="User Login">
			<div v-for="(item, index) in login_data" :key="index">
				<b-input-group class="mb-2 mt-2">
					<b-input-group-prepend is-text>
						<b-icon :icon="item.icon"></b-icon>
					</b-input-group-prepend>
					<b-form-input
						:type="item.type"
						:placeholder="item.placeholder"
						v-model="item.value"
					></b-form-input>
				</b-input-group>
			</div>

			<b-button variant="success" block class="mt-3">Login</b-button>
		</b-card>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
export default {
	name: 'LoginView',
	components: {
		HeaderVue,
	},
	data() {
		return {
			login_data: [
				{
					name: 'NIN',
					label: 'nin',
					type: 'text',
					icon: 'person-fill',
					value: '',
					placeholder: 'Enter NIN',
				},
				{
					name: 'Password',
					label: 'password',
					type: 'password',
					icon: 'lock-fill',
					value: '',
					placeholder: 'Enter Password',
				},
			],
		};
	},
};
</script>

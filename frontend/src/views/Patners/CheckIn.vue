<template>
	<div class="">
		<header-vue />
		<b-card class="mx-auto mt-3" title="Check NIN">
			<div v-for="(item, index) in checkin_data" :key="index">
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

			<b-button variant="success" block class="mt-3">Check In</b-button>
		</b-card>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
export default {
	name: 'PartnerCheckIn',
	components: {
		HeaderVue,
	},
	data() {
		return {
			checkin_data: [
				{
					name: 'NIN',
					label: 'nin',
					type: 'text',
					icon: 'person-fill',
					value: '',
					placeholder: 'Enter NIN',
				},
				{
					name: 'Passcode',
					label: 'passcode',
					type: 'password',
					icon: 'upc-scan',
					value: '',
					placeholder: 'Enter Pascode',
				},
			],
		};
	},
};
</script>

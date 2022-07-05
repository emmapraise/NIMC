<template>
	<div>
		<b-form-input
			list="citizen-list"
			v-model="result"
			@change="comboboxEvent()"
		></b-form-input>

		<datalist id="citizen-list">
			<option v-for="(item, index) in citizens" :key="index">
				{{ item.user.nin }} {{ item.user.first_name }}
				{{ item.user.last_name }}
			</option>
		</datalist>
	</div>
</template>
<script>
export default {
	name: 'UserCombobox',
	props: ['citizens'],
	data() {
		return {
			result: '',
			user: {},
		};
	},
	mounted() {},
	methods: {
		comboboxEvent() {
			const nin = this.result.split(' ')[0];
			this.user = this.citizens.find((o) => o.user.nin === nin);
		},
	},
};
</script>

<template>
	<div>
		<b-form-input
			list="citizen-list"
			v-model="result"
			@change="comboboxEvent()"
		></b-form-input>

		<datalist id="citizen-list">
			<option v-for="(item, index) in nininfo" :key="index">
				{{ item.citizen.user.nin }} {{ item.citizen.user.first_name }}
				{{ item.citizen.user.last_name }}
			</option>
		</datalist>
		<div style="display: none">
			{{ nininfo }}
		</div>
	</div>
</template>
<script>
export default {
	name: 'UserCombobox',
	props: ['nininfo'],
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
			this.user = this.nininfo.find((obj) => obj.citizen.user.nin === nin);
			this.$emit('combobox', this.user);
		},
	},
};
</script>

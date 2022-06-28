<template>
	<div class="">
		<b-row>
			<b-col md="6" v-for="(item, index) in name_tab" :key="index" class="my-1">
				<b-row>
					<b-col md="3">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col md="9">
						<div v-if="isProfilePage"></div>
						<div v-else>
							<div v-if="item.type === 'radio'">
								<b-form-radio-group
									:id="item.label"
									v-model="item.value"
									required
									@input="emitValue"
									:options="item.options"
								></b-form-radio-group>
							</div>
							<div v-else>
								<b-form-input
									:id="item.label"
									:type="item.type"
									@input="emitValue"
									v-model="item.value"
									required
								></b-form-input>
							</div></div></b-col></b-row></b-col
		></b-row>
	</div>
</template>
<script>
export default {
	name: 'NameComponet',
	props: ['userDispatch'],
	data() {
		return {
			name_tab: [
				{
					name: 'Surname',
					label: 'surname',
					type: 'text',
					value: '',
				},
				{
					name: 'First Name',
					label: 'last_name',
					type: 'text',
					value: '',
				},
				{
					name: 'Middle Name',
					label: 'middle_name',
					type: 'text',
					value: '',
				},
				{
					name: 'Gender',
					label: 'gender',
					type: 'radio',
					value: null,
					options: [
						{ value: 'M', text: 'Male' },
						{ value: 'F', text: 'Female' },
					],
				},
				{
					name: 'Email',
					label: 'email',
					type: 'email',
					value: '',
				},
				{
					name: 'Phone',
					label: 'phone_number',
					type: 'tel',
					value: '',
				},
			],
			isProfilePage: false,
		};
	},
	mounted() {
		this.name_tab = this.userDispatch;
	},
	methods: {
		emitValue() {
			const data = this.name_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.$emit('userData', data);
		},
	},
};
</script>

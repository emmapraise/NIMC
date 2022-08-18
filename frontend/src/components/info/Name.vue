<template>
	<div class="">
		<b-row>
			<b-col md="6" v-for="(item, index) in name_tab" :key="index" class="my-1">
				<b-row>
					<b-col md="4">
						<label :for="item.label">{{ item.name }}</label></b-col
					>
					<b-col md="8">
						<div v-if="edit">
							<div v-if="item.type === 'radio'">
								<b-form-radio-group
									:id="item.label"
									v-model="item.value"
									required
									@input="emitValue"
									:options="item.options"
								></b-form-radio-group>
							</div>
							<div v-else-if="item.type === 'file'">
								<uploadfile :file="item.value" />
							</div>
							<div v-else>
								<b-form-input
									:id="item.label"
									:type="item.type"
									@input="emitValue"
									v-model="item.value"
									required
								></b-form-input>
							</div>
						</div>
						<div v-else>
							<div v-if="item.label === 'gender'">
								<template> {{ item.value | convertGender }} </template>
							</div>
							<div v-else>
								{{ item.value }}
							</div>
						</div>
					</b-col></b-row
				></b-col
			></b-row
		>
	</div>
</template>
<script>
import uploadfile from '../file/uploadfile.vue';
export default {
	components: { uploadfile },
	name: 'NameComponet',
	props: {
		getData: Object,
		isAdmin: Boolean,
		edit: Boolean,
	},
	filters: {
		convertGender: function (value) {
			return value === 'F' ? 'Female' : 'Male';
		},
	},
	data() {
		return {
			name_tab: [
				{
					name: 'Avatar',
					label: 'avatar',
					type: 'file',
					value: null,
				},
				{
					name: 'Surname',
					label: 'last_name',
					type: 'text',
					value: '',
				},
				{
					name: 'First Name',
					label: 'first_name',
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
					label: 'phone',
					type: 'tel',
					value: '',
				},
			],
		};
	},
	created() {
		this.loadData();
	},
	mounted() {},
	computed: {
		getLabel(e) {
			return e.label;
		},
	},
	methods: {
		emitValue() {
			const data = this.name_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			data.password = process.env.VUE_APP_DEFAULT_PASSWORD;
			this.$emit('userData', data);
		},
		loadData() {
			const user = this.getData.citizen['user'];
			this.name_tab.map((item) => {
				//convert apiObj to array to perform filter on it
				const asArray = Object.entries(user);
				//filter out the key and value whose key isEqual the value of label from objArray
				const filtered = asArray.filter(([key]) => key === item['label']);
				//convert the key and value array to object
				const justStrings = Object.fromEntries(filtered);
				//set the value of each item in ObjArray to the value of the object whose key is the same as the value of each item.label
				return (item['value'] = justStrings[item['label']]);
			});
		},
	},
};
</script>
